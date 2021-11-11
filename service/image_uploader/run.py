import yadisk
import config
import os
from flask import Flask, request
import datetime
import sys

app = Flask(__name__)

y = yadisk.YaDisk(token="AQAAAABWSz6LAAd-6FZnFpIosUEYsbzsTnLlDsE")
assert y.check_token()  # Проверим токен


def safe_mkdir(path):
    if not y.exists(path):
        # print("create folder with current date", file=sys.stderr)
        y.mkdir(path)


@app.route("/upload_images", methods=["GET", "POST"])
def upload_images():
    request_time = request.form["time"]
    user_id = str(request.form["user_id"])

    # create date folder
    current_date_folder = os.path.join(
        config.yadisk_images_path, datetime.datetime.now().strftime("%Y-%m-%d")
    )
    # print("current_date_folder", current_date_folder, file=sys.stderr)

    safe_mkdir(current_date_folder)
    safe_mkdir(os.path.join(current_date_folder, user_id))
    # safe_mkdir(os.path.join(current_date_folder, user_id, request_time))

    path_to_input_image = os.path.join(
        config.images_path, request_time, "input.jpg"
    )

    # path_to_input_image = os.path.join(
    #     config.images_path, request_time, f"input_{request_time}.jpg"
    # )

    # print("path_to_input_image", path_to_input_image, file=sys.stderr)
    # print("path_to_result_image", path_to_result_image, file=sys.stderr)

    yadisk_upload_path = os.path.join(current_date_folder, user_id)

    try:
        y.upload(
            path_to_input_image, yadisk_upload_path + f"/{request_time}.jpg"
        )
    except FileNotFoundError:
        pass
    return "1"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
