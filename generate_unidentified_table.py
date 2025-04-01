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
            max-width: 95vw;
            width: 95vw;
            margin: 0 auto;
            overflow-x: hidden;
        }}
        h1 {{
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        .table-container {{
            width: 100% !important;
            overflow-x: auto;
        }}
        table {{
            width: 100%;
            table-layout: auto;
            white-space: nowrap;
        }}
        thead th {{
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            color: white;
            padding: 6px;
            font-size: 14px;
        }}
        th, td {{
            padding: 6px;
            text-align: center;
            border-bottom: 1px solid #eaeaea;
        }}
        tr:hover {{
            background-color: #f9f9f9;
        }}
        img {{
            width: 200px;
            height: auto;
            border-radius: 6px;
        }}

        td img {{
            display: block;
            margin: 0 auto;
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
    </style>
</head>
<body>
<div class="container">
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Sr. No.</th>
                    <th>Fossil Name</th>
                    <th>Fossil Image</th>
                    <th>Top 5 Predictions</th>
                    <th>Selection</th>
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
            radios.forEach(radio => {{ if (radio.checked) {{ selected = radio.value; }}}});

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
            <td><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/unidentified/page_{key}/" target="_blank">{key}</a></td>
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