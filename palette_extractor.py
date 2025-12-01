import numpy as np
from sklearn.cluster import KMeans
from utils import rgb_to_hex

class PaletteExtractor:

    def __init__(self, num_colors=5):
        self.num_colors = num_colors

    def extract_palette(self, image):
        """Extract dominant colors using K-Means clustering."""

        # Reshape image → (num_pixels, 3)
        pixels = image.reshape(-1, 3)

        # Apply K-Means
        kmeans = KMeans(n_clusters=self.num_colors, random_state=42)
        kmeans.fit(pixels)

        # Cluster centers are dominant colors
        colors = kmeans.cluster_centers_.astype(int)

        # Convert to HEX format
        hex_colors = [rgb_to_hex(c) for c in colors]

        return colors, hex_colors
