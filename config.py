import os

root = os.environ.get("PRJPATH", "")


TIME_FORMAT = "%Y-%m-%d_%H-%M-%S"
images_path = os.path.join(root, "images")
