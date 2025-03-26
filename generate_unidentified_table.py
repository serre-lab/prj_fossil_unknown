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
        /* General Styles */
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f4f7f8;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }}

        .container {{
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
        }}

        h1 {{
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }}

        h3, h4 {{
            color: #2c3e50;
            margin-top: 20px;
        }}

        p {{
            color: #555555;
            margin-bottom: 15px;
        }}

        ul {{
            margin-left: 20px;
        }}

        ul li {{
            margin-bottom: 10px;
        }}

        /* Table Styles */
        .table-container {{
            max-height: 600px;
            overflow-y: auto;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background-color: #fff;
        }}

        thead th {{
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            color: white;
            padding: 12px;
            font-size: 14px;
        }}

        th, td {{
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #eaeaea;
        }}

        tr:hover {{
            background-color: #f9f9f9;
        }}

        img {{
            width: 80px;
            height: auto;
            border-radius: 8px;
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
    <h1>Unidentified Fossils Predictions Table</h1>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width: 5%;">Sr. No.</th>
                    <th style="width: 10%;">Fossil Name</th>
                    <th style="width: 20%;">Fossil Image</th>
                    <th style="width: 25%;">Top 5 Predictions</th>
                    <th style="width: 10%;">Plausible</th>
                    <th style="width: 10%;">Impossible</th>
                    <th style="width: 10%;">Not Sure</th>
                    <th style="width: 10%;">Not Applicable</th>
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

            // Get the selected radio button in the row
            let radios = row.querySelectorAll('input[type="radio"]');
            
            radios.forEach((radio) => {{
                if (radio.checked) {{
                    selected = radio.value; // Get the value of the selected radio button
                }}
            }});

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
        <td><input type="radio" name="row{index}" value="Plausible"></td>
        <td><input type="radio" name="row{index}" value="Impossible"></td>
        <td><input type="radio" name="row{index}" value="Not Sure"></td>
        <td><input type="radio" name="row{index}" value="Not Applicable"></td>
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
        <td><input type="radio" name="row{index}" value="Plausible"></td>
        <td><input type="radio" name="row{index}" value="Impossible"></td>
        <td><input type="radio" name="row{index}" value="Not Sure"></td>
        <td><input type="radio" name="row{index}" value="Not Applicable"></td>
    </tr>
    """
    table_rows += row

# Create the final HTML file
html_content = html_template.format(table_rows=table_rows)

# Save to an HTML file
with open("./docs/unidentified_table.md", "w") as f:
    f.write(html_content)

print("HTML file generated: unidentified_table.md")