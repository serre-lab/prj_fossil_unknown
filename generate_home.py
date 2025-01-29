import json

IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Classification</title>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f4f7f8;
            color: #333;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 95%;
            margin: 30px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            text-align: center;
            font-size: 28px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        
        thead th {{
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            color: white;
            font-size: 14px;
            font-weight: 600;
            padding: 16px;
            z-index: 2;
        }}

        .table-container {{
            max-height: 600px;
            overflow-y: auto;
            overflow-x: hidden;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            position: relative;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            border-radius: 10px;
            background: #fff;
            table-layout: fixed;
        }}

        thead {{
            position: sticky;
            top: 0;
            z-index: 10;
            background-color: #2c3e50;
        }}

        th, td {{
            padding: 14px;
            text-align: center;
            border-bottom: 1px solid #e0e0e0;
            word-wrap: break-word;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        img {{
            width: 100px;
            height: 100px;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }}
        input[type="checkbox"] {{
            width: 18px;
            height: 18px;
            cursor: pointer;
        }}
        .fixed-button {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            color: white;
            padding: 14px 24px;
            border: none;
            border-radius: 30px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }}
        .fixed-button:hover {{
            background: linear-gradient(135deg, #45A049, #2E7D32);
            transform: scale(1.05);
        }}

        /* Ensuring images are uniform */
        .td img {{
            width: 100px;
            height: 100px;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }}

        /* Making the header stick properly */
        .thead {{
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            z-index: 10;
        }}

    </style>
</head>
<body>
<div class="container">
    <div class="guide">
        <h2>🍃 Website Navigation Guide 🔍</h2>

        <h3>📋 Overview</h3>
        <p>Welcome to our Unknown Fossil Classification Documentation! This guide will help you navigate and interact with our comprehensive fossil prediction system.</p>

        <h3>🌟 How to Use the Website</h3>

        <h4>1. Understanding the Prediction Table 📊</h4>
        <ul>
            <li>The table displays a comprehensive list of unknown fossils</li>
            <li>Each row contains:
                <ul>
                    <li>Fossil name (clickable hyperlink)</li>
                    <li>Fossil image</li>
                    <li>Top 5 predictions</li>
                    <li>Interactive classification options</li>
                </ul>
            </li>
        </ul>

        <h4>2. Fossil Name Details 🔬</h4>
        <ul>
            <li>Clicking the fossil name opens a detailed information page</li>
            <li>Page includes:
                <ul>
                    <li>Full fossil image</li>
                    <li>Model predictions</li>
                    <li>Top 10 key visual concepts influencing the prediction</li>
                    <li>Each concept is a hyperlink to our Fossil Lens website, showing detail information of that particular concept</li>
                </ul>
            </li>
        </ul>

        <h4>3. Prediction Interaction 🤔</h4>
        <p>For each fossil prediction, you can:</p>
        <ul>
            <li>✅ Mark as "Correct" if the prediction seems accurate</li>
            <li>❌ Mark as "Incorrect" if predictions are clearly wrong</li>
            <li>🤷‍♀️ Select "Maybe" if you're unsure</li>
        </ul>

        <h4>4. Response Tracking 💾</h4>
        <ul>
            <li>Use the "Download Responses" button (bottom right)</li>
            <li>Saves your classification choices as a JSON file</li>
            <li><strong>Important</strong>: Download before closing the website, as responses aren't saved</li>
        </ul>

        <h4>5. Resuming Your Work 🔄</h4>
        <ul>
            <li>Next visit: Use serial numbers to continue where you left off</li>
        </ul>

        <p>Enjoy exploring the fascinating world of leaf fossil classification! 🍂🌿</p>
    </div>
    <p> </p>
    <h1>Unknown Fossils Predictions Table</h1>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width: 10$;">Sr. No.</th>
                    <th style="width: 15%;">Fossil Name</th>
                    <th style="width: 15%;">Fossil Image</th>
                    <th style="width: 30%;">Top 5 Predictions</th>
                    <th style="width: 10%;">Correct</th>
                    <th style="width: 10%;">Incorrect</th>
                    <th style="width: 10%;">Maybe</th>
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
            if (cells[4].querySelector("input").checked) selected = "Correct";
            if (cells[5].querySelector("input").checked) selected = "Incorrect";
            if (cells[6].querySelector("input").checked) selected = "Maybe";

            data.push({{
                "Serial Number": index + 1,
                "Fossil Name": fossilName,
                "User Selection": selected
            }});
        }});

        let blob = new Blob([JSON.stringify(data, null, 2)], {{ type: "application/json" }});
        let a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "fossil_responses.json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }}
</script>

</body>
</html>
"""

# Load image names from JSON
with open("image_names2.json", "r") as file:
    image_names = json.load(file)

with open("image2_predictions.json", 'r') as file:
    image_predictions = json.load(file)

# Generate table rows dynamically

table_rows = ""
for index, (key, value) in enumerate(image_predictions.items(), start=1):
    predictions_html = "<br>".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
    <tr>
        <td>{index}</td>
        <td><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/page_{key}/" target="_blank">{key}</a></td>
        <td><img src="{IMAGE_URL.format(key)}" alt="Fossil Image"></td>
        <td>{predictions_html}</td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    """
    table_rows += row


# Create the final HTML file
html_content = html_template.format(table_rows=table_rows)

# Save to an HTML file
with open("./docs/index.md", "w") as f:
    f.write(html_content)

print("HTML file generated: index.md")