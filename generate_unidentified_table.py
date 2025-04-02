import json

IMAGE_URL = "https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/{}.jpg"
UNKNOWN_IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unidentified Fossils Predictions Table</title>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f4f7f8;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }}
        .container {{
            max-width: 100%;
            width: 100%;
            margin: 0 auto;
            overflow-x: auto;
        }}
        h1 {{
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        .table-container {{
            width: 100%;
        }}
        table {{
            width: 100%;
        }}
        thead th {{
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            font-size: 18px;
        }}
        th, td {{
            padding: 10px;
            text-align: center;
            border-bottom: 1px solid #eaeaea;
            font-size: 16px;
        }}
        tr:hover {{
            background-color: #f9f9f9;
        }}
        img {{
            width: 100%; /* Make it responsive */
            max-width: 100%; /* Prevents overflow */
            height: auto;
            display: block;
            margin: auto;
            border-radius: 6px;
        }}
        .radio-container {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .fixed-button {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 30px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }}
        .fixed-button:hover {{
            background-color: #45a049;
        }}

        .md-sidebar.md-sidebar--secondary{{
            width: 0px !important;
        }}

        /* Responsive adjustments */
        @media (max-width: 768px) {{
            th, td {{
                font-size: 14px;
                padding: 8px;
            }}
            img {{
                width: 150px;
            }}
        }}
        @media (max-width: 480px) {{
            th, td {{
                font-size: 12px;
                padding: 5px;
            }}
            img {{
                width: 120px;
            }}
            .fixed-button {{
                font-size: 14px;
                padding: 12px 24px;
            }}
        }}
    </style>
</head>
<body>
<div class="container">
    <h1>Unidentified Fossils Predictions Table</h1>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width: 2%;">Sr. No.</th>
                    <th style="width: 8%;">Fossil Name</th>
                    <th style="width: 50%;">Fossil Image</th>
                    <th style="width: 10%;">Top 5 Predictions</th>
                    <th style="width: 30%;">Selection</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>
</div>

<button class="fixed-button" onclick="downloadJSON()">Download Responses</button>

<script>
    function downloadJSON() {{
        let rows = document.querySelectorAll("tbody tr");
        let data = [];

        rows.forEach((row, index) => {{
            let cells = row.querySelectorAll("td");
            let fossilName = cells[1].innerText;
            let selected = null;
            let radios = row.querySelectorAll('input[type="radio"]');
            radios.forEach(radio => {{ if (radio.checked) {{ selected = radio.value; }} }});

            data.push({{
                "Serial Number": index + 1,
                "Fossil Name": fossilName,
                "User Selection": selected
            }});
        }});

        let blob = new Blob([JSON.stringify(data, null, 2)], {{ type: "application/json" }});
        let a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "unidentified_fossil_responses.json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }}
</script>
</body>
</html>
"""


with open("image2_predictions.json", 'r') as file:
    unknown_image_predictions = json.load(file)


with open("unidentified_fossil_predictions.json", 'r') as file:
    image_predictions = json.load(file)



# Generate table rows dynamically
table_rows = ""

for index, (key, value) in enumerate(unknown_image_predictions.items(), start=1):
    predictions_html = "<br>".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
        <tr>
            <td>{index}</td>
            <td><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/unknown/page_{key}/" target="_blank">{key}</a></td>
            <td><img src="{UNKNOWN_IMAGE_URL.format(key)}" alt="Fossil Image"></td>
            <td>{predictions_html}</td>
            <td>
                <label><input type="radio" name="row{index}" value="Plausible">Plausible</label><br>
                <label><input type="radio" name="row{index}" value="Impossible">Impossible</label><br>
                <label><input type="radio" name="row{index}" value="Not Sure">Not Sure</label><br>
                <label><input type="radio" name="row{index}" value="Not Applicable">NA</label>
            </td>
        </tr>
        """

    table_rows += row
total_unknown_images = len(unknown_image_predictions)
for index, (key, value) in enumerate(image_predictions.items(), start=1):
    index = total_unknown_images + index
    predictions_html = "<br>".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
    <tr>
        <td>{index}</td>
        <td><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/unidentified/page_{key}/" target="_blank">{key}</a></td>
        <td><img src="{IMAGE_URL.format(key)}" alt="Fossil Image"></td>
        <td>{predictions_html}</td>
        <td>
            <label><input type="radio" name="row{index}" value="Plausible">Plausible</label><br>
            <label><input type="radio" name="row{index}" value="Impossible">Impossible</label><br>
            <label><input type="radio" name="row{index}" value="Not Sure">Not Sure</label><br>
            <label><input type="radio" name="row{index}" value="Not Applicable">NA</label>
        </td>
    </tr>
    """
    table_rows += row

# Create the final HTML file
html_content = html_template.format(table_rows=table_rows)

# Save to an HTML file
with open("./docs/unidentified_table.md", "w") as f:
    f.write(html_content)

print("HTML file generated: unidentified_table.md")