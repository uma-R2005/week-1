from PIL import Image, ImageDraw

def create_sample_image():
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)

    # Draw some colored rectangles
    draw.rectangle([0, 0, 100, 100], fill=(255, 0, 0))       # Red top-left
    draw.rectangle([100, 0, 200, 100], fill=(0, 255, 0))     # Green top-right
    draw.rectangle([0, 100, 100, 200], fill=(0, 0, 255))     # Blue bottom-left
    draw.rectangle([100, 100, 200, 200], fill=(255, 255, 0)) # Yellow bottom-right

    img.save('sample.jpg')
    print("sample.jpg created!")

if __name__ == "__main__":
    create_sample_image()
