import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def download_images(url_list, save_dir):
    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    for url in url_list:
        try:
            # Extract image filename from URL
            image_name = url.split("/")[-2]+'.png'
            filename = os.path.basename(urlparse(url).path)
            save_path = os.path.join(save_dir, image_name)

            # Download the image
            response = requests.get(url)
            response.raise_for_status()  # Raise error for bad status

            # Write image to file
            with open(save_path, 'wb') as f:
                f.write(response.content)

            print(f"Saved: {save_path}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# Example usage
url_list = [
    "https://storage.googleapis.com/serrelab/prj_fossils/Paper-Figure-3/Berberidaceae_fossil_sae_concepts6/fossil_Berberidaceae_Mahonia_marginata_Florissant_FLFO_010069A/concept_9_1034.png"
]


save_dir = "/Users/gg1313/Desktop/Research/fossils/figure3_assets/reference_concept_1034/fossils"  # Replace with your desired directory
download_images(url_list, save_dir)
