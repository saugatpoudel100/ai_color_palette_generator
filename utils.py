import cv2  #used for read image and convert color formats
import numpy as np #used for number calculations and handling pixel data
import matplotlib.pyplot as plt # show images and color palettes

def load_image(image_path):
    """Load and image from disk and convert BGR to RGB."""
    image = cv2.imread(image_path) #read the image
    if image is None:
        raise ValueError("Image not found")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #change BGR into RGB beacuse matplotlib understand RGB
    return image

def rgb_to_hex(color):
    """convert and rgb tuple to hex format."""

    RGB =(120,40,200)
    HEX = "#7828c8"
    r, g, b = int(color[0]), int(color[1]), int(color[2])
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def show_palette(colors):
    """Show a horizontal palette of colors using Matplotlib."""
    plt.figure(figsize=(10, 2))
    plt.title("Generated Color Palette")

    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i + 1)
        plt.imshow([[color]])
        plt.axis('off')

    plt.show()