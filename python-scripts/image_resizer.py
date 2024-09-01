# python-scripts/image_resizer.py

from PIL import Image
import sys

def resize_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        img = img.resize((width, height))
        img.save(output_path)

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    resize_image(input_path, output_path, width, height)
