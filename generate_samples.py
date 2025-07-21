from constants import (
    berberidaceae_samples, berberidaceae_tree, berberidaceae_leaf_examples, berberidaceae_fossil_examples,
    juglandaceae_samples, juglandaceae_tree, juglandaceae_leaf_examples, juglandaceae_fossil_examples
)

import json

def generate_markdown(class_name, concepts, reference_examples, leaf_triplets, fossil_triplets, output_path="concepts_visualization.md"):
    
    def captioned_clickable_img(concept_name, path, width="300px"):
        return (
            f"<div style='text-align: center;'>"
            f"<div style='font-size: 14px; margin-bottom: 4px; color: #4bac49;'>{concept_name}</div>"
            f"<a href='{path}' target='_blank'>"
            f"<img src='{path}' style='width:{width}; margin: 5px; border-radius: 8px; border: 1px solid #888;' />"
            f"</a></div>"
        )
    
    def markdown_clickable_img(concept_name, path, width="300px"):
        return (
            f"<div style='text-align: center; display: inline-block; margin: 10px;'>"
            f"<div style='font-size: 14px; margin-bottom: 4px; color: #4bac49;'>{concept_name}</div>"
            f"<a href='{path}' target='_blank'>"
            f"<img src='{path}' style='width:{width}; margin: 5px; border-radius: 8px; border: 1px solid #888; "
            f"transition: transform 0.3s ease;' "
            f"onmouseover='this.style.transform=\"scale(1.5)\"' "
            f"onmouseout='this.style.transform=\"scale(1)\"' />"
            f"</a></div>"
        )
    
    def markdown_concept_clickable_img(concept_name, path, url,width="300px"):
        return (
            f"<div style='text-align: center; display: inline-block; margin: 10px;'>"
            f"<div style='font-size: 14px; margin-bottom: 4px; color: #4bac49;'>{concept_name}</div>"
            f"<a href='{url}' target='_blank'>"
            f"<img src='{path}' style='width:{width}; margin: 5px; border-radius: 8px; border: 1px solid #888; "
            f"transition: transform 0.3s ease;' "
            f"onmouseover='this.style.transform=\"scale(2.0)\"' "
            f"onmouseout='this.style.transform=\"scale(1)\"' />"
            f"</a></div>"
        )

    def make_image_row(images, concept_name="Concept", width="200px"):
        return (
            "<div style='display: flex; gap: 20px; flex-wrap: wrap;'>\n" +
            "\n".join([
                captioned_clickable_img("", img, width)
                for img in images
            ]) + "\n</div>"
        )

    def checkbox(sample_type, sample_name):
        return (
            f"<label style='display: block; margin: 10px 0;'>"
            f"<input type='checkbox' name='{sample_type}' value='{sample_name}' /> Select <b>{sample_name}</b>"
            f"</label>"
        )

    def js_download_block():
        return f"""
<script>
function downloadSelections() {{
    const leaf = [];
    const fossil = [];

    document.querySelectorAll("input[name='leaf']:checked").forEach(el => leaf.push(el.value));
    document.querySelectorAll("input[name='fossil']:checked").forEach(el => fossil.push(el.value));

    const data = {{ leaf, fossil }};
    const filename = "{class_name}_selected_samples.json";
    const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}}
</script>

<button onclick="downloadSelections()" style="padding: 10px 20px; background: #333; color: white; border: none; border-radius: 5px; cursor: pointer; margin: 20px 0;">
Download Selected Samples as JSON
</button>
"""

    with open(output_path, 'w') as f:
        # Title and Instructions
        f.write(f"# {class_name} Concept Review for Paper Inclusion\n\n")
        f.write("This page presents two learned visual concepts, along with sample leaf and fossil images that exhibit these concepts. You can help us **selecting samples where both concepts are clearly represented**, then click the download button.\n")
        f.write("Here is how you can do it. Go throught the visual concepts and use the reference samples to understand the concepts. Then, go through the leaf and fossil review sections and select the samples where both concepts are clearly represented.\n")

        # Concept Images
        f.write("## 1. Visual Concepts\n\n")
        f.write("<div style='display: flex; gap: 40px;'>\n")
        f.write(markdown_concept_clickable_img(f"Concept - {concept_name['concept1']}", concepts['concept1'], concept_page['concept1'], width="400px") + "\n")
        f.write(markdown_concept_clickable_img(f"Concept - {concept_name['concept2']}", concepts['concept2'], concept_page['concept2'], width="400px") + "\n")
        f.write("</div>\n\n")

        # Reference Examples
        for i, concept_key in enumerate(["concept1", "concept2"], 1):
            f.write(f"## 2.{i} Reference Samples for Concept {concept_name[concept_key]}\n\n")

            f.write("### Leaf Samples\n")
            f.write(make_image_row(reference_examples[concept_key]["leaves"], concept_name=f"Concept {i} — Leaf"))
            f.write("\n\n")

            f.write("### Fossil Samples\n")
            f.write(make_image_row(reference_examples[concept_key]["fossils"], concept_name=f"Concept {i} — Fossil"))
            f.write("\n\n")

        # Leaf Review Section
        f.write("## 3. Leaf Review Section\n\n")
        for triplet in leaf_triplets:
            # f.write(f"### Leaf: {triplet['sample_name']}\n\n")
            f.write(checkbox("leaf", f"{triplet['sample_name']}") + "\n\n")
            f.write("<div style='display: flex; gap: 20px;'>\n")
            f.write(markdown_clickable_img(f"{concept_name['concept1']}", triplet['concept1']))
            f.write(markdown_clickable_img(f"{concept_name['concept2']}", triplet['concept2']))
            f.write("</div>\n")
            # f.write(checkbox("leaf", triplet['sample_name']) + "\n")
            f.write("<br><br>\n")

        # Fossil Review Section
        f.write("## 4. Fossil Review Section\n\n")
        for triplet in fossil_triplets:
            # f.write(f"### Fossil: {triplet['sample_name']}\n\n")
            f.write(checkbox("fossil", f"{triplet['sample_name']}") + "\n\n")
            f.write("<div style='display: flex; gap: 20px;'>\n")
            f.write(markdown_clickable_img(f"{concept_name['concept1']}", triplet['concept1']))
            f.write(markdown_clickable_img(f"{concept_name['concept2']}", triplet['concept2']))
            f.write("</div>\n")
            # f.write(checkbox("fossil", triplet['sample_name']) + "\n")
            f.write("<br><br>\n")

        # Add JS Download Button
        f.write("---\n")
        f.write(js_download_block())

        f.write("\n\n---\n")
        f.write("**Thank you for your review!** Select your samples above and download them using the button.\n")



def find_image_by_concept(files, concept_number):
    for f in files:
      if f.endswith(f"_{concept_number}.png"):
        return f
    return None



concept1 = "506"
concept2 = "1034"

reference_examples = {
    "concept1": {
        "leaves": berberidaceae_leaf_examples[concept1],
        "fossils": berberidaceae_fossil_examples[concept1][:6]
    },
    "concept2": {
        "leaves": berberidaceae_leaf_examples[concept2],
        "fossils": berberidaceae_fossil_examples[concept2][:6]
    }
}

fossil_dir = f"https://storage.googleapis.com/serrelab/prj_fossils/Paper-Figure-3/Berberidaceae_fossil_sae_concepts6/"
leaf_dir = f"https://storage.googleapis.com/serrelab/prj_fossils/Paper-Figure-3/Berberidaceae_leaf_sae_concepts6/"

leaf_folders = {leaf: leaf_dir + leaf for leaf in berberidaceae_samples['leaf']}
fossil_folders = {fossil: fossil_dir + fossil for fossil in berberidaceae_samples['fossil']}

leaf_files = {leaf: berberidaceae_tree['Berberidaceae_leaf_sae_concepts6'][leaf]['__files__'] for leaf in berberidaceae_samples['leaf']}
fossil_files = {fossil: berberidaceae_tree['Berberidaceae_fossil_sae_concepts6'][fossil]['__files__'] for fossil in berberidaceae_samples['fossil']}

leaf_c1 = []
leaf_c2 = []
for leaf, concepts in leaf_files.items():
    cn = find_image_by_concept(concepts, concept1)
    cn2 = find_image_by_concept(concepts, concept2)
    url = leaf_dir + leaf + "/" + cn
    url2 = leaf_dir + leaf + "/" + cn2
    leaf_c1.append(url)
    leaf_c2.append(url2)

fossil_c1 = []
fossil_c2 = []
for fossil, concepts in fossil_files.items():
    cn = find_image_by_concept(concepts, concept1)
    cn2 = find_image_by_concept(concepts, concept2)
    url = fossil_dir + fossil + "/" + cn
    url2 = fossil_dir + fossil + "/" + cn2
    fossil_c1.append(url)
    fossil_c2.append(url2)

concept_name = {
    "concept1": concept1,
    "concept2": concept2
}
concept_page = {
    "concept1": f"https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20{concept1}/",
    "concept2": f"https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20{concept2}/",
}
concepts = {
    "concept1": f"https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_{concept1}_fv.webp",
    "concept2": f"https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_{concept2}_fv.webp",
}

leaf_triplets = [
    {"concept1": leaf_c1[i], "concept2": leaf_c2[i], "sample_name": leaf_c1[i].split("/")[-2][7:]}
    for i in range(10)
]

fossil_triplets = [
    {"concept1": fossil_c1[i], "concept2": fossil_c2[i], "sample_name": fossil_c1[i].split("/")[-2][7:]}
    for i in range(10)
]

class_name = "Berberidaceae"
generate_markdown(class_name, concepts, reference_examples, leaf_triplets, fossil_triplets, output_path="docs/figure_sample/berberidaceae.md")
