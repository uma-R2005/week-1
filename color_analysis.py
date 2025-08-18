from PIL import Image, ImageDraw
from collections import Counter

def main():
    # Load and resize image (resize to speed up processing)
    try:
        image = Image.open("sample.jpg")  # Change this to your image file
    except FileNotFoundError:
        print("Image file not found. Please check the filename.")
        return

    image = image.resize((100, 100))
    pixels = list(image.getdata())

    # Count RGB values using tuples
    color_counts = Counter(pixels)
    most_common = color_counts.most_common(1)[0]  # Returns (color_tuple, count)

    print(f"Most common color: {most_common[0]} (appeared {most_common[1]} times)")

    # Show a swatch of the most common color
    swatch = Image.new("RGB", (100, 100), most_common[0])
    swatch.show()

if __name__ == "__main__":
    main()
