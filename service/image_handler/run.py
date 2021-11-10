import os

import clip
from images_classes import (
    en_dishes_classes,
    en_non_food_classes,
    food_not_food_classes,
)
import torch
from PIL import Image
from flask import Flask, request
import json

import config

app = Flask(__name__)


def apply_clip(image):
    # Prepare the inputs
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)

    # first classify food/no food
    similarity = (100.0 * image_features @ food_or_no_embeds.T).softmax(dim=-1)
    values, indices = similarity[0].topk(2)
    image_is_food = food_not_food_classes[indices[0]] == "food"

    if image_is_food:
        similarity = (100.0 * image_features @ food_classes_embeds.T).softmax(
            dim=-1
        )
        values, indices = similarity[0].topk(5)
        class_name = en_dishes_classes[indices[0]]
    else:
        similarity = (
            100.0 * image_features @ non_food_classes_embeds.T
        ).softmax(dim=-1)
        values, indices = similarity[0].topk(5)
        class_name = en_non_food_classes[indices[0]]

    response = dict()
    response["image_is_food"] = image_is_food
    response["class_name"] = class_name
    return json.dumps(response)

    # Print the result
    # print("\nTop predictions:\n")
    # for value, index in zip(values, indices):
    #     print(f"{eats_classes[index]:>16s}: {100 * value.item():.2f}%")


@app.route("/return_message", methods=["GET", "POST"])
def return_message():
    request_time = request.form["time"]
    path_to_input_image = os.path.join(
        config.images_path, request_time, "input.jpg"
    )
    image = Image.open(open(path_to_input_image, "rb"))
    result = apply_clip(image)
    return result


def prepare_captions_embeddings(captions):
    embeds = model.encode_text(
        torch.cat([clip.tokenize(f"a photo of a {c}") for c in captions]).to(
            device
        )
    )
    embeds /= embeds.norm(dim=-1, keepdim=True)
    return embeds


if __name__ == "__main__":
    device = "cpu"
    model, preprocess = clip.load("ViT-B/32", device)
    food_or_no_embeds = prepare_captions_embeddings(food_not_food_classes)
    food_classes_embeds = prepare_captions_embeddings(en_dishes_classes)
    non_food_classes_embeds = prepare_captions_embeddings(en_non_food_classes)
    app.run(host="0.0.0.0", debug=True)
