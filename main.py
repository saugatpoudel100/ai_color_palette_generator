from utils import load_image, show_palette
from palette_extractor import PaletteExtractor

def main():
    print("=== AI Color Palette Generator ===")
    image_path = input("Enter the image path: ")

    # Load image
    image = load_image(image_path)

    # Create extractor
    extractor = PaletteExtractor(num_colors=5)

    # Extract palette
    colors, hex_colors = extractor.extract_palette(image)

    # Print results
    print("\nGenerated Color Palette (HEX):")
    for hex_code in hex_colors:
        print(hex_code)

    # Show palette"
    show_palette(colors)


if __name__ == "__main__":
    main()
