import os
import json

# Constants
NUM_IMAGES = 943
PROJECT_DIR = "./"
DOCS_DIR = os.path.join(PROJECT_DIR, "docs")
IMAGES_DIR = os.path.join(DOCS_DIR, "images")
PAGES_DIR = os.path.join(DOCS_DIR, "pages")
MKDOCS_YML = os.path.join(PROJECT_DIR, "mkdocs.yml")
IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"
CONCEPT_URL = "https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_{}/{}"
CONCEPT_INFO = "https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20{}/"
# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)

# Load image names from JSON
with open("image_names.json", "r") as file:
    image_names = json.load(file)

with open("image_predictions.json", 'r') as file:
    image_predictions = json.load(file)

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image and Predictions</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: #333;
            background-color: #f8f8f8;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2 {{
            text-align: center;
            color: #000;
        }}
        .image-name {{
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
            color: #000;
        }}
        .predictions {{
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .divider {{
            width: 100%;
            margin: 30px auto;
            border-top: 1px solid #ddd;
        }}
        .main-image-container {{
            text-align: center;
            margin: 30px 0;
        }}
        .main-image-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .concept-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 0 auto;
        }}
        .concept-image {{
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .concept-image:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }}
        .concept-image img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        .concept-caption {{
            padding: 10px;
            font-size: 14px;
            color: #333;
            font-weight: bold;
            text-align: center;
        }}
    </style>
</head>
<body>
    <h1>Image and Concept Predictions</h1>
    <div class="image-name">Image Name: <strong>{image_name}</strong></div>
    <div class="predictions">
        Top 5 Predictions: {class1}, {class2}, {class3}, {class4}, {class5}
    </div>
    <div class="divider"></div>
    <div class="main-image-container">
        <h2>Main Image</h2>
        <img src="{main_image}" alt="Fossil Image" style="width: 300px; height: 600px; object-fit: contain;>
    </div>
    <div class="divider"></div>
    <div class="concept-grid">
        {concept_images}
    </div>
</body>
</html>
"""

# Generate Markdown pages with inline HTML
for i, (key, value) in enumerate(image_names.items()):
    class1, class2, class3, class4, class5 = image_predictions[key]
    concept_images = "\n".join(
        [f'''<div class="concept-image">
            <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                <img src="{CONCEPT_URL.format(key, value[j])}" alt="Concept Image {j+1}">
            </a>
            <div class="concept-caption">{value[j]}</div>
        </div>'''
 for j in range(10)]
    )
    html_content = html_template.format(
        image_name=f"Image {key}",
        class1 = class1,
        class2 = class2,
        class3 = class3,
        class4 = class4,
        class5 = class5,
        main_image=IMAGE_URL.format(key),
        concept_images=concept_images
    )
    page_path = os.path.join(PAGES_DIR, f"page_{key}.md")
    print(page_path)
    with open(page_path, "w") as f:
        f.write(html_content)

# Generate MkDocs configuration
with open(MKDOCS_YML, "w") as f:
    f.write("site_name: Unknown Fossil Predictions\n")
    f.write("theme:\n")
    f.write("  name: material\n")
    f.write("  logo: images/logo.png\n")
    f.write("  favicon: images/logo.png\n")
    f.write("  palette:\n")
    f.write("    primary: black\n")
    f.write("    accent: white\n")
    f.write("nav:\n")
    f.write("  - Home: index.md\n")
    for i, key in enumerate(image_names.keys()):
        f.write(f"  - {key}: pages/page_{key}.md\n")

# Create index page
index_path = os.path.join(DOCS_DIR, "index.md")
with open(index_path, "w") as f:
    f.write("# Unknown Fossil Predictions!\n\n")
    f.write("Navigate through the sidebar to view all images.\n")
