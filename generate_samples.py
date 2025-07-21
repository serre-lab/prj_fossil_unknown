from constants import berberidaceae_samples,berberidaceae_tree, berberidaceae_leaf_examples, berberidaceae_fossil_examples, juglandaceae_samples, juglandaceae_tree, juglandaceae_leaf_examples, juglandaceae_fossil_examples

def generate_markdown(triplets, output_path="concepts_visualization.md"):
    """
    Generate a clean and professional markdown file visualizing leaf-concept-fossil triplets,
    with minimal whitespace and maximally sized images.
    """
    main_img_width = 99  # percent of cell/table width, for max size
    sample_img_width = 110  # big, but not crowding

    with open(output_path, 'w') as f:
        f.write("# Concept Visualizations\n\n")
        f.write("_Visualizations showing shared concepts between extant leaves and fossil samples._\n\n")
        f.write("<hr>\n")
        
        for i, triplet in enumerate(triplets):
            f.write("\n\n---\n\n")
            f.write(f"## Sample {i+1}\n\n")
            
            for j, concept in enumerate(triplet["concepts"]):
                leaf_desc = f"<span style='color:#2A5D3E;font-weight:600;'>Leaf: <em>{concept['leaf_name'][7:]}</em></span>"
                fossil_desc = f"<span style='color:#7A4B22;font-weight:600;'>Fossil: <em>{concept['fossil_name'][7:]}</em></span>"
                concept_desc = f"<span style='color:#2F4CD6;font-weight:600;'>Concept: {concept['concept_name']}</span>"

                if j == 0:
                    f.write(f"### {leaf_desc}<br>{fossil_desc}\n\n")
                
                f.write(f"**{concept_desc}**\n\n")
                
                # Remove border-spacing, use largest possible image
                f.write(f"""
<table align="center" style="margin:0 auto 10px auto; border-spacing:0; width:100%; table-layout:fixed;">
<tr>
    <td align="center" style="padding:0;">
        <b>Leaf</b><br>
        <a href="{concept['leaf_main']}" target="_blank">
            <img src="{concept['leaf_main']}" style="width:{main_img_width}%; min-width:220px; max-width:500px; height:auto; border-radius:14px; box-shadow:0 2px 12px #ccc; display:block; margin: 0 auto;">
        </a>
    </td>
    <td align="center" style="padding:0;">
        <b>Concept</b><br>
        <a href="{concept['concept_main']}" target="_blank">
            <img src="{concept['concept_main']}" style="width:{main_img_width}%; min-width:240px; max-width:600px; height:auto; border-radius:14px; box-shadow:0 2px 12px #ccc; display:block; margin: 0 auto;">
        </a>
    </td>
    <td align="center" style="padding:0;">
        <b>Fossil</b><br>
        <a href="{concept['fossil_main']}" target="_blank">
            <img src="{concept['fossil_main']}" style="width:{main_img_width}%; min-width:220px; max-width:500px; height:auto; border-radius:14px; box-shadow:0 2px 12px #ccc; display:block; margin: 0 auto;">
        </a>
    </td>
</tr>
</table>
""")
                
                # Similar leaf samples
                f.write("<div style='margin-bottom:4px; font-weight:600;'>Similar Leaf Samples</div>\n")
                f.write('<div style="display: flex; flex-wrap: wrap; gap: 6px 6px; margin-bottom:8px; justify-content:left;">\n')
                for url in concept["leaf_samples"]:
                    f.write(
                        f"<a href='{url}' target='_blank'>"
                        f"<img src='{url}' style='width:{sample_img_width}px; height:{sample_img_width}px; object-fit:cover; border-radius:8px; box-shadow:0 1px 4px #eee; display:inline-block; margin:0;'></a>\n"
                    )
                f.write("</div>\n")

                # Similar fossil samples
                f.write("<div style='margin-top:2px; font-weight:600;'>Similar Fossil Samples</div>\n")
                f.write('<div style="display: flex; flex-wrap: wrap; gap: 6px 6px; margin-bottom:10px; justify-content:left;">\n')
                for url in concept["fossil_samples"]:
                    f.write(
                        f"<a href='{url}' target='_blank'>"
                        f"<img src='{url}' style='width:{sample_img_width}px; height:{sample_img_width}px; object-fit:cover; border-radius:8px; box-shadow:0 1px 4px #eee; display:inline-block; margin:0;'></a>\n"
                    )
                f.write("</div>\n")

        f.write("\n<hr>\n")
        f.write('<div style="font-size:13px; color:#999;">Auto-generated on Sunday, July 20, 2025, 5:45 PM PDT</div>\n')

    print(f"✅ Clean Markdown saved to `{output_path}`")



def find_image_by_concept(files, concept_number):
    for f in files:
      if f.endswith(f"_{concept_number}.png"):
        return f
    return None

fossil_dir = f"https://storage.googleapis.com/serrelab/prj_fossils/Paper-Figure-3/Juglandaceae_fossil_sae_concepts6/"
leaf_dir = f"https://storage.googleapis.com/serrelab/prj_fossils/Paper-Figure-3/Juglandaceae_leaf_sae_concepts6/"
concept_url = "https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_{concept_number}_fv.webp"

concept1 = "1810"
concept2 = "899"

leaf_folders = {leaf: leaf_dir + leaf for leaf in juglandaceae_samples['leaf']}
fossil_folders = {fossil: fossil_dir + fossil for fossil in juglandaceae_samples['fossil']}

leaf_files = {leaf: juglandaceae_tree['Juglandaceae_leaf_sae_concepts6'][leaf]['__files__'] for leaf in juglandaceae_samples['leaf']}
fossil_files = {fossil: juglandaceae_tree['Juglandaceae_fossil_sae_concepts6'][fossil]['__files__'] for fossil in juglandaceae_samples['fossil']}

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

triplets = []

n = min(len(leaf_c1), len(leaf_c2), len(fossil_c1), len(fossil_c2), 10)
for k in range(n):
    concepts = []
    for i, concept in enumerate([concept1, concept2]):
        if i == 0:
            leaf = leaf_c1[k]
            fossil = fossil_c1[k]
        else:
            leaf = leaf_c2[k]
            fossil = fossil_c2[k]
        leaf_name = leaf.split("/")[-2]
        fossil_name = fossil.split("/")[-2]
        concepts.append({
            "leaf_main": leaf,
            "concept_main": concept_url.format(concept_number=concept),
            "fossil_main": fossil,
            "leaf_name": leaf_name,
            "fossil_name": fossil_name,
            "concept_name": concept,
            "leaf_samples": juglandaceae_leaf_examples[concept],
            "fossil_samples": juglandaceae_fossil_examples[concept][:6],
        })
    triplets.append({
        "concepts": concepts
    })


# triplets = [
#     {
#         "concepts": [
#             {
#                 "leaf_main": "https://.../leaf1.webp",
#                 "concept_main": "https://.../concept1.webp",
#                 "fossil_main": "https://.../fossil1.webp",
#                 "leaf_samples": ["https://.../leaf1_s1.webp", "..."],
#                 "fossil_samples": ["https://.../fossil1_s1.webp", "..."],
#                 "leaf_name": "Leaf1",
#                 "fossil_name": "Fossil1",
#                 "concept_name": "Concept506"
#             },
#             {
#                 "leaf_main": "https://.../leaf2.webp",
#                 "concept_main": "https://.../concept2.webp",
#                 "fossil_main": "https://.../fossil2.webp",
#                 "leaf_samples": ["https://.../leaf2_s1.webp", "..."],
#                 "fossil_samples": ["https://.../fossil2_s1.webp", "..."],
#                 "leaf_name": "Leaf2",
#                 "fossil_name": "Fossil2",
#                 "concept_name": "Concept1034"
#             }
#         ]
#     },
#     # Add more triplets if needed
# ]

generate_markdown(triplets, output_path="docs/figure_sample/juglandaceae.md")
