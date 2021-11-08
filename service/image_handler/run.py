import clip
import torch

import os
import config
import cv2

from flask import Flask, request

app = Flask(__name__)

app.route("/return_message", methods=["GET", "POST"])


def return_message():
    request_time = request.form["time"]
    path_to_input_image = os.path.join(
        config.images_path, request_time, "input.jpg"
    )
    print(path_to_input_image)
    image = cv2.imread(path_to_input_image)[..., ::-1]
    # result = cropper.process(image)

    # res_path = os.path.join(config.images_path, request_time, "result.jpg")
    # cv2.imwrite(res_path, result[:, :, ::-1] * 255)
    return "0"


if __name__ == "__main__":
    device = "cpu"
    model, preprocess = clip.load("ViT-B/32", device)
    app.run(host="0.0.0.0", debug=True)
