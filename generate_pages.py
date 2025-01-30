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
CONCEPT_URL = "https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_{}/{}"
FEATURE_VIS_URL = "https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_{}_fv.webp"
CONCEPT_INFO = "https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20{}/"
CLASS_INFO = "https://fel-thomas.github.io/Leaf-Lens/classes/{}/"
# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)

# Load image names from JSON
with open("image_names2.json", "r") as file:
    image_names = json.load(file)

with open("image2_predictions.json", 'r') as file:
    image_predictions = json.load(file)

# HTML Template
# html_template = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Image and Predictions</title>
#     <style>
#         body {{
#             font-family: 'Helvetica Neue', Arial, sans-serif;
#             margin: 0;
#             padding: 0;
#             line-height: 1.6;
#             color: #333;
#             background-color: #f8f8f8;
#         }}
#         .container {{
#             max-width: 1200px;
#             margin: 0 auto;
#             padding: 40px 20px;
#         }}
#         h1, h2 {{
#             text-align: center;
#             color: #2c3e50;
#             margin-bottom: 30px;
#         }}
#         .image-name {{
#             font-size: 24px;
#             text-align: center;
#             margin-bottom: 30px;
#             color: #2c3e50;
#         }}
#         .predictions {{
#             text-align: center;
#             font-size: 18px;
#             margin-bottom: 40px;
#             background-color: #fff;
#             padding: 20px;
#             border-radius: 10px;
#             box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         }}
#         .divider {{
#             width: 80%;
#             margin: 40px auto;
#             border-top: 1px solid #e0e0e0;
#         }}
#         .main-image-container {{
#             text-align: center;
#             margin: 40px 0;
#         }}
#         .main-image-container img {{
#             max-width: 100%;
#             height: auto;
#             border-radius: 10px;
#             box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#         }}
#         .concept-grid {{
#             display: grid;
#             grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
#             gap: 30px;
#             margin: 0 auto;
#         }}
#         .concept-image {{
#             background-color: #fff;
#             border-radius: 10px;
#             overflow: hidden;
#             transition: transform 0.3s ease, box-shadow 0.3s ease;
#             box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         }}
#         .concept-image:hover {{
#             transform: translateY(-5px);
#             box-shadow: 0 8px 15px rgba(0,0,0,0.15);
#         }}
#         .concept-image img {{
#             width: 100%;
#             height: auto;
#             display: block;
#         }}
#         .concept-caption {{
#             padding: 15px;
#             font-size: 16px;
#             color: #2c3e50;
#             font-weight: 600;
#             text-align: center;
#         }}
#     </style>
# </head>
# <body>
#     <div class="container">
#         <h1>Image and Concept Predictions</h1>
#         <div class="image-name">Image Name: <strong>{image_name}</strong></div>
#         <div class="predictions">
#             <h2>Top 5 Predictions</h2>
#             <p>{class1}, {class2}, {class3}, {class4}, {class5}</p>
#         </div>
#         <div class="divider"></div>
#         <div class="main-image-container">
#             <h2>Main Image</h2>
#             <img src="{main_image}" alt="Fossil Image" style="width: 300px; height: 600px; object-fit: contain;">
#         </div>
#         <div class="divider"></div>
#         <h2>Concept Images</h2>
#         <div class="concept-grid">
#             {concept_images}
#         </div>
#     </div>
# </body>
# </html>
# """

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image and Predictions</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
        }}
        .container {{
            max-width: 100%;
            margin: 20px auto;
            padding: 20px;
        }}
        h1, h2 {{
            text-align: center;
            color: #2c3e50;
        }}
        .image-name, .predictions {{
            text-align: center;
            margin-bottom: 20px;
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .main-image-container {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .main-image-container img {{
            width: 300px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .concept-card {{
            width: 100%; /* Full width of the container */
            max-width: 900px; /* Increased max width */
            padding: 30px; /* More padding for better spacing */
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .concept-container {{
            display: flex;
            flex-direction: column;
            gap: 100px;
        }}

        .concept-card:hover {{
            transform: scale(1.07);
            box-shadow: 0 8px 16px rgba(0,0,0,0.25);
        }}

        .concept-images {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }}

        .concept-images img {{
            width: 400px;
            height: 400px;
            object-fit: contain;
            border-radius: 10px;
        }}

        .concept-images img:hover {{
            transform: scale(1.5);
            transition: transform 0.3s ease;
            box-shadow: 0 8px 16px rgba(0,0,0,0);
        }}

        .concept-caption {{
            text-align: center;
            font-weight: bold;
            margin-top: 15px;
            width: 100%;
            font-size: 1.2em;
        }}

        .predictions a {{
            text-decoration: none;
            color: green;
            font-weight: bold;
            transition: color 0.3s ease, transform 0.2s ease;
        }}

        .predictions a:hover {{
            color: blue;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Image and Concept Predictions</h1>
        <div class="image-name">Image Name: <strong>{image_name}</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class1}/" target="_blank"><em> {class1} </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class2}/" target="_blank"><em> {class2} </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class3}/" target="_blank"><em> {class3} </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class4}/" target="_blank"><em> {class4} </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/{class5}/" target="_blank"><em> {class5} </em></a>
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="{main_image}" alt="Fossil Image">
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            {concept_images}
        </div>
    </div>
</body>
</html>
"""


# Generate Markdown pages with inline HTML
for i, (key, value) in enumerate(image_names.items()):
    class1, class2, class3, class4, class5 = image_predictions[key]
    value.sort(key = lambda x : int(x.split("_")[1]))
    concept_images = "\n".join(
        [f'''<div class="concept-card">
                <div class="concept-images">
                    <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                        <img src="{CONCEPT_URL.format(key, value[j])}" alt="Concept Image {j+1}">
                    </a>
                    <a href="{CONCEPT_INFO.format(value[j].split("_")[-1][:-4])}" target="_blank">
                        <img src="{FEATURE_VIS_URL.format(value[j].split("_")[-1][:-4])}" alt="Feature Visualization {j+1}">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: {value[j].split("_")[-1][:-4]}</em>, Relative_rank:  {value[j].split("_")[-2]}</div>
            </div>''' for j in range(len(value))]
    )

    html_content = html_template.format(
        image_name=f"{key}",
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
    f.write("site_name: Unidentified Fossil Predictions\n")
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
    f.write("# Unidentified Fossil Predictions!\n\n")
    f.write("Navigate through the sidebar to view all images.\n")
