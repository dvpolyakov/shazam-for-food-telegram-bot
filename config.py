import os

root = os.environ.get("PRJPATH", "")
yadisk_images_path = "/shazam_for_food_images"
TOP_K = 3
CLASS_PROBA_THRESHOLD = 5
TIME_FORMAT = "%Y-%m-%d_%H-%M-%S"
images_path = os.path.join(root, "images")
