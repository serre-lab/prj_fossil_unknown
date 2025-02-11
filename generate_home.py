import json

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Classification</title>
    <style>
        /* General Styles */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f4f7f8;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }

        h3, h4 {
            color: #2c3e50;
            margin-top: 20px;
        }

        p {
            color: #555555;
            margin-bottom: 15px;
        }

        ul {
            margin-left: 20px;
        }

        ul li {
            margin-bottom: 10px;
        }

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

        /* Flex container for GIF */
        .flex-gif {
            display: flex; /* Use flexbox */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            margin-top: 20px; /* Add some spacing above */
        }

        /* Styling for GIF container */
        .gif-intro {
            width: auto; /* Allow flexibility for resizing */
            text-align: center; /* Center content inside */
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2); /* Add shadow for elegance */
            border-radius: 3%; /* Rounded corners */
            overflow: hidden; /* Prevent content overflow */
        }

        /* Styling for GIF image */
        .gif-intro img {
            max-width: 100%; /* Ensure it doesn't exceed container width */
            width: 400px; /* Set a larger width for better visibility */
            height: auto; /* Maintain aspect ratio */
            display: block; /* Center the image inside the div */
        }

    </style>
</head>
<body>
<div class="container">
    <h1>🍃 Website Navigation Guide 🔍</h1>
    
    <div class = "flex-gif">
        <div class = "gif-intro">
            <img src="images/fossil.gif" alt="Navigation Guide GIF">
        </div>
    </div>

    <h3>📑 Metadata (Google Spreadsheet)</h3>
    <ul>
        <li><a href = "https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank">Florissant CU Metadata </a></li>
        <li><a href = "https://docs.google.com/spreadsheets/d/1o7OIcT5ikbqbk5bJIWYm-jesXnIc5whp/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank">Florissant FLFO Metadata</a></li>
    </ul>
    <h3>📋 Overview</h3>
    <p>Welcome to our Unidentified Fossil Classification Documentation! This guide will help you navigate our website and understand our machine learning models' predictions for unidentified fossils.</p>

    <h3>🌟 How to Use the Website</h3>

    <h4>1. Understanding the Prediction Table 📊</h4>
    <ul>
        <li>The table displays a comprehensive list of unidentified fossils.</li>
        <li>Each row contains:
          <ul>
              <li>Fossil name (clickable hyperlink)</li>
              <li>Fossil image</li>
              <li>Top five predictions (clickable hyperlink)</li>
              <li>Interactive classification options</li>
          </ul>
        </li>
    </ul>

    <h4>2. Fossil Name Details 🔬</h4>
    <ul>
        <li>Clicking the fossil name opens a detailed information page.</li>
        <li>The page includes:
          <ul>
              <li>Full fossil image</li>
              <li>Model predictions</li>
              <li>Top ten key visual concepts influencing the prediction</li>
              <li>Hyperlinks to detailed concept pages on our Fossil Lens website</li>
          </ul>
        </li>
    </ul>

    <h4>3. Prediction Interaction 🤔</h4>
    <p>You can interact with each fossil prediction by:</p>
    <ul>
      <li><strong>✅ Marking as "Correct"</strong></li>
      <li><strong>❌ Marking as "Incorrect"</strong></li>
      <li><strong>🤷‍♀️ Selecting "Maybe"</strong></li>
    </ul>

    <h4>4. Response Tracking 💾</h4>
    <ul>
      <li>Use the "Download Responses" button (bottom right) to save your choices as a JSON file.</li>
      <li><strong>Important:</strong> Download before closing the website to avoid losing responses.</li>
    </ul>

    <h4>5. Resuming Your Work 🔄</h4>
    <ul>
      <li>You can resume work using serial numbers during your next visit.</li>
    </ul>

    <p><em>Enjoy exploring the fascinating world of leaf fossil classification! 🍂🌿</em></p>
</div>

</body>
</html>

"""

# Save to an HTML file
with open("./docs/index.md", "w") as f:
    f.write(html_template)

print("HTML file generated: index.md")