import os

import clip
from images_classes import en_all_classes_list
import torch
from PIL import Image
from flask import Flask, request

import config

app = Flask(__name__)


def apply_clip(image):
    # Prepare the inputs
    image_input = preprocess(image).unsqueeze(0).to(device)

    text_inputs = torch.cat(
        [clip.tokenize(f"a photo of a {c}") for c in en_all_classes_list]
    ).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(5)
    return en_all_classes_list[indices[0]]

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


if __name__ == "__main__":
    device = "cpu"
    model, preprocess = clip.load("ViT-B/32", device)
    app.run(host="0.0.0.0", debug=True)
