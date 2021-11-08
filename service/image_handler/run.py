import clip
import torch

import os
import config

# import cv2
from service.image_handler.images_classes import eats_classes_dict
from flask import Flask, request
from PIL import Image


app = Flask(__name__)

app.route("/return_message", methods=["GET", "POST"])


def apply_clip(image):
    # Prepare the inputs
    image_input = preprocess(image).unsqueeze(0).to(device)
    en_dishes_names, ru_dishes_names = list(eats_classes_dict.keys()), list(
        eats_classes_dict.values()
    )
    text_inputs = torch.cat(
        [clip.tokenize(f"a photo of a {c}") for c in en_dishes_names]
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
    return ru_dishes_names[indices[0]]

    # Print the result
    # print("\nTop predictions:\n")
    # for value, index in zip(values, indices):
    #     print(f"{eats_classes[index]:>16s}: {100 * value.item():.2f}%")


@app.route("/return_message", methods=["GET", "POST"])
def return_message():
    print("request recieved")
    request_time = request.form["time"]
    path_to_input_image = os.path.join(
        config.images_path, request_time, "input.jpg"
    )
    print(path_to_input_image)
    image = Image.open(open(path_to_input_image, "rb"))
    print(type(image))
    result = apply_clip(image)
    # return result
    return result
    # res_path = os.path.join(config.images_path, request_time, "result.jpg")
    # cv2.imwrite(res_path, result[:, :, ::-1] * 255)


if __name__ == "__main__":
    device = "cpu"
    model, preprocess = clip.load("ViT-B/32", device)
    app.run(host="0.0.0.0", debug=True)
