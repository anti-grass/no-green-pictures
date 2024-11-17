import sys
from PIL import Image

def process_image(input_image_path):
    try:
        image = Image.open(input_image_path).convert("RGBA")
        pixels = image.load()

        for y in range(image.height):
            for x in range(image.width):
                r, g, b, a = pixels[x, y]
                if g > max(r, b):
                    pixels[x, y] = (0, 0, 0, a)

        output_path = "output_" + input_image_path
        image.save(output_path)
        print(f"Processed image saved as: {output_path}")

    except FileNotFoundError:
        print(f"File not found: {input_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <image_file>")
    else:
        input_image = sys.argv[1]
        process_image(input_image)