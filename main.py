from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./img"
path_out = "/edited_img"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpen image
    edit = img.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(filename)[0]

    # enhance
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    edit.save(f".{path_out}/{clean_name}_edited.jpg")