import json

IMAGE_URL = "https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/{}.jpg"
UNKNOWN_IMAGE_URL = "https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/{}/image.jpg"

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Leaf Lens - Feedback Table</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(to bottom, #f8f9fa 0%, #ffffff 100%);
            color: #1a1a1a;
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }}

        .page-header {{
            text-align: center;
            padding: 40px 20px 30px;
            margin-bottom: 20px;
            border-bottom: 1px solid #e8e8e8;
        }}

        .page-header h1 {{
            font-size: 36px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }}

        .page-header p {{
            font-size: 16px;
            color: #666;
            margin-top: 10px;
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
            padding: 20px;
        }}

        .table-wrapper {{
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
            overflow: hidden;
        }}

        .table-container {{
            width: 100%;
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        thead th {{
            position: sticky;
            top: 0;
            background: linear-gradient(to bottom, #2563eb 0%, #1d4ed8 100%);
            color: white;
            padding: 16px 12px;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            text-align: center;
            z-index: 10;
        }}

        tbody tr {{
            transition: all 0.2s ease;
            border-bottom: 1px solid #f0f0f0;
        }}

        tbody tr:nth-child(even) {{
            background-color: #fafbfc;
        }}

        tbody tr:hover {{
            background-color: #f0f7ff;
            transform: scale(1.005);
            border-left: 3px solid #2563eb;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.08);
        }}

        td {{
            padding: 14px 12px;
            text-align: center;
            font-size: 14px;
            color: #4a4a4a;
            vertical-align: middle;
        }}

        .serial-number {{
            font-weight: 700;
            color: #2563eb;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 8px !important;
            border-radius: 6px;
        }}

        .fossil-name {{
            min-width: 150px;
        }}

        .fossil-name a {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.2s ease;
            border-bottom: 1px solid rgba(37, 99, 235, 0.2);
        }}

        .fossil-name a:hover {{
            color: #1d4ed8;
            border-bottom-color: #1d4ed8;
        }}

        .fossil-image {{
            padding: 10px;
        }}

        .fossil-image img {{
            max-width: 200px;
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }}

        .fossil-image img:hover {{
            transform: scale(1.05);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        }}

        .predictions {{
            max-width: 250px;
            text-align: left;
            counter-reset: prediction-counter;
        }}

        .predictions a {{
            display: flex;
            align-items: center;
            color: #2563eb;
            text-decoration: none;
            font-size: 13px;
            margin-bottom: 6px;
            padding: 6px 10px;
            border-radius: 6px;
            transition: all 0.2s ease;
            background: #f0f7ff;
            border-left: 3px solid #2563eb;
        }}

        .predictions a:hover {{
            background-color: #e0f2fe;
            color: #1d4ed8;
            transform: translateX(4px);
            border-left-color: #1d4ed8;
        }}

        .predictions a::before {{
            content: counter(prediction-counter);
            counter-increment: prediction-counter;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 20px;
            height: 20px;
            background: #2563eb;
            color: white;
            border-radius: 50%;
            font-size: 11px;
            font-weight: 700;
            margin-right: 8px;
            flex-shrink: 0;
        }}

        .radio-group {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            align-items: center;
        }}

        .radio-group label {{
            cursor: pointer;
            font-size: 13px;
            color: #4a4a4a;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 6px;
            transition: all 0.2s ease;
            width: 100%;
            justify-content: center;
            font-weight: 500;
        }}

        .radio-group label:hover {{
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }}

        /* Color-coded labels */
        .radio-group label:has(input[value="Plausible"]) {{
            background-color: #d1fae5;
            color: #065f46;
            border: 1px solid #6ee7b7;
        }}

        .radio-group label:has(input[value="Plausible"]):hover {{
            background-color: #a7f3d0;
            color: #034e3a;
        }}

        .radio-group label:has(input[value="Impossible"]) {{
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fca5a5;
        }}

        .radio-group label:has(input[value="Impossible"]):hover {{
            background-color: #fecaca;
            color: #7f1d1d;
        }}

        .radio-group label:has(input[value="Not Sure"]) {{
            background-color: #fef3c7;
            color: #92400e;
            border: 1px solid #fcd34d;
        }}

        .radio-group label:has(input[value="Not Sure"]):hover {{
            background-color: #fde68a;
            color: #78350f;
        }}

        .radio-group label:has(input[value="Not Applicable"]) {{
            background-color: #f3f4f6;
            color: #4b5563;
            border: 1px solid #d1d5db;
        }}

        .radio-group label:has(input[value="Not Applicable"]):hover {{
            background-color: #e5e7eb;
            color: #374151;
        }}

        /* Selected state styling */
        .radio-group label:has(input:checked) {{
            font-weight: 600;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
        }}

        /* Row completion indicator */
        tbody tr:has(input:checked) {{
            background-color: #f0fdf4 !important;
            border-left: 4px solid #22c55e;
        }}

        tbody tr:has(input:checked):hover {{
            background-color: #dcfce7 !important;
        }}

        .radio-group input[type="radio"] {{
            cursor: pointer;
            margin-right: 4px;
            accent-color: currentColor;
        }}

        /* Legend/legend styling */
        .feedback-legend {{
            display: none;
        }}

        .fixed-button {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(to bottom, #2563eb 0%, #1d4ed8 100%);
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
            transition: all 0.3s ease;
            z-index: 1000;
        }}

        .fixed-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
        }}

        .md-sidebar.md-sidebar--secondary {{
            width: 0px !important;
        }}

        /* Responsive adjustments */
        @media (max-width: 1200px) {{
            thead th {{
                font-size: 12px;
                padding: 12px 8px;
            }}
            
            td {{
                font-size: 13px;
                padding: 12px 8px;
            }}

            .fossil-image img {{
                max-width: 150px;
            }}
        }}

        @media (max-width: 768px) {{
            .page-header {{
                padding: 30px 15px 20px;
            }}

            .page-header h1 {{
                font-size: 28px;
            }}

            .container {{
                padding: 10px;
            }}

            thead th {{
                font-size: 11px;
                padding: 10px 6px;
            }}

            td {{
                font-size: 12px;
                padding: 10px 6px;
            }}

            .fossil-image img {{
                max-width: 120px;
            }}

            .fixed-button {{
                bottom: 20px;
                right: 20px;
                padding: 12px 20px;
                font-size: 13px;
            }}
        }}

        @media (max-width: 480px) {{
            .page-header h1 {{
                font-size: 24px;
            }}

            thead th {{
                font-size: 10px;
                padding: 8px 4px;
            }}

            td {{
                font-size: 11px;
                padding: 8px 4px;
            }}

            .fossil-image img {{
                max-width: 100px;
            }}

            .predictions {{
                max-width: 150px;
            }}
        }}
    </style>
</head>
<body>
<div class="page-header">
    <h1>Fossil Leaf Lens Feedback</h1>
    <p>Please provide feedback on the predicted fossil identifications</p>
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px; flex-wrap: wrap; font-size: 13px;">
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #d1fae5; border: 1px solid #6ee7b7; border-radius: 4px;"></span>
            <span style="color: #065f46;"><strong>Plausible</strong> - One or more families are likely correct</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #fee2e2; border: 1px solid #fca5a5; border-radius: 4px;"></span>
            <span style="color: #991b1b;"><strong>Impossible</strong> - No predictions make sense</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #fef3c7; border: 1px solid #fcd34d; border-radius: 4px;"></span>
            <span style="color: #92400e;"><strong>Not Sure</strong> - Further study needed</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="display: inline-block; width: 16px; height: 16px; background: #f3f4f6; border: 1px solid #d1d5db; border-radius: 4px;"></span>
            <span style="color: #4b5563;"><strong>Not Applicable</strong> - Specimen doesn't belong</span>
        </div>
    </div>
</div>

<div class="container">
    <div class="table-wrapper">
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th style="width: 5%;">No.</th>
                        <th style="width: 12%;">Fossil Name</th>
                        <th style="width: 25%;">Fossil Image</th>
                        <th style="width: 20%;">Top 5 Predictions</th>
                        <th style="width: 38%;">Your Feedback</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
    </div>
</div>

<button class="fixed-button" onclick="downloadJSON()">📥 Download Responses</button>

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
    predictions_html = "".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
        <tr>
            <td class="serial-number">{index}</td>
            <td class="fossil-name"><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/unknown/page_{key}/" target="_blank">{key}</a></td>
            <td class="fossil-image"><img src="{UNKNOWN_IMAGE_URL.format(key)}" alt="Fossil Image"></td>
            <td><div class="predictions">{predictions_html}</div></td>
            <td>
                <div class="radio-group">
                    <label><input type="radio" name="row{index}" value="Plausible"> Plausible</label>
                    <label><input type="radio" name="row{index}" value="Impossible"> Impossible</label>
                    <label><input type="radio" name="row{index}" value="Not Sure"> Not Sure</label>
                    <label><input type="radio" name="row{index}" value="Not Applicable"> Not Applicable</label>
                </div>
            </td>
        </tr>
        """

    table_rows += row
total_unknown_images = len(unknown_image_predictions)
for index, (key, value) in enumerate(image_predictions.items(), start=1):
    index = total_unknown_images + index
    predictions_html = "".join([f'<a href="https://fel-thomas.github.io/Leaf-Lens/classes/{p}/" target="_blank">{p}</a>' for p in value])
    row = f"""
    <tr>
        <td class="serial-number">{index}</td>
        <td class="fossil-name"><a href="https://serre-lab.github.io/prj_fossil_unknown/pages/unidentified/page_{key}/" target="_blank">{key}</a></td>
        <td class="fossil-image"><img src="{IMAGE_URL.format(key)}" alt="Fossil Image"></td>
        <td><div class="predictions">{predictions_html}</div></td>
        <td>
            <div class="radio-group">
                <label><input type="radio" name="row{index}" value="Plausible"> Plausible</label>
                <label><input type="radio" name="row{index}" value="Impossible"> Impossible</label>
                <label><input type="radio" name="row{index}" value="Not Sure"> Not Sure</label>
                <label><input type="radio" name="row{index}" value="Not Applicable"> Not Applicable</label>
            </div>
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