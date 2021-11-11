import os

import clip
from images_classes import (
    en_dishes_classes,
    en_non_food_classes,
    food_not_food_classes,
    en_beverage_classes,
)
import torch
from PIL import Image
from flask import Flask, request
import json

import config

app = Flask(__name__)


def get_classes_probas(result_values, result_indices, subclass_names_list):
    classes_probas = dict()
    for value, index in zip(result_values, result_indices):
        classes_probas[subclass_names_list[index]] = round(100 * value.item())
    return classes_probas


def apply_clip(image):
    # Prepare the inputs
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)

    # first classify food/beverage/no food
    similarity = (100.0 * image_features @ food_or_no_embeds.T).softmax(dim=-1)
    values, indices = similarity[0].topk(3)
    object_type = food_not_food_classes[indices[0]]

    if object_type == "food":
        similarity = (100.0 * image_features @ food_classes_embeds.T).softmax(
            dim=-1
        )
        values, indices = similarity[0].topk(config.TOP_K)
        subclass_names_list = en_dishes_classes
        # class_name = en_dishes_classes[indices[0]]
    elif object_type == "beverage":
        similarity = (
            100.0 * image_features @ beverage_classes_embeds.T
        ).softmax(dim=-1)
        values, indices = similarity[0].topk(config.TOP_K)
        subclass_names_list = en_beverage_classes
        # class_name = en_beverage_classes[indices[0]]
    else:
        similarity = (
            100.0 * image_features @ non_food_classes_embeds.T
        ).softmax(dim=-1)
        values, indices = similarity[0].topk(config.TOP_K)
        subclass_names_list = en_non_food_classes
        # class_name = en_non_food_classes[indices[0]]

    classes_probas = get_classes_probas(values, indices, subclass_names_list)

    response = dict()
    response["object_type"] = object_type
    response["classes_probas"] = classes_probas
    return json.dumps(response)


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
    with torch.no_grad():

        embeds = model.encode_text(
            torch.cat(
                [clip.tokenize(f"a photo of a {c}") for c in captions]
            ).to(device)
        )
        embeds /= embeds.norm(dim=-1, keepdim=True)
    return embeds


if __name__ == "__main__":
    device = "cpu"
    model, preprocess = clip.load("ViT-B/32", device)
    food_or_no_embeds = prepare_captions_embeddings(food_not_food_classes)
    food_classes_embeds = prepare_captions_embeddings(en_dishes_classes)
    beverage_classes_embeds = prepare_captions_embeddings(en_beverage_classes)
    non_food_classes_embeds = prepare_captions_embeddings(en_non_food_classes)
    app.run(host="0.0.0.0", debug=True)
