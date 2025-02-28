
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

    <h3><em> Welcome to our website! </em></h3>
    <p>We are excited to share the fruits of years of research and innovation aimed at solving one of paleobotany's most challenging puzzles: identifying fossil angiosperm leaves, which are abundant yet notoriously difficult to classify, especially in the absence of organic attachments or cuticles, due to their complexity, variation, and the often limited quality of available images. Through the power of AI and computer vision, we have developed a deep learning model that synthesizes photorealistic fossil images from modern, cleared, and x-rayed leaves. This approach allows machine identifications of fossil and extant leaves at the family level, the starting point for most investigations, with levels of accuracy sufficient to provide useful suggestions for experts.</p>
    <p>Initially, to limit the immense variation in leaf preservation among fossil sites, we present the tool for leaf fossils from a single, extraordinarily well-studied and photo-documented site: Florissant Fossil Beds, late Eocene of Colorado. The images were gathered over many years by Dr. Herbert Meyer (retired, National Parks Service) from museums around the world, as explained in Wilf et al. <a href = "https://doi.org/10.3897/phytokeys.187.723502021" target="_blank"> 2021</a> (PhytoKeys), who made a vetted subset of Florissant fossils available as part of a large <a href = "https://doi.org/10.25452/figshare.plus.14980698.v2" target="_blank">image collection</a> of living and fossil leaves.</a></p>
    <p>On this website, we share the  results  of our model for hundreds of hard-to-identify fossil leaves from Florissant that were not included in the 2021 vetted subset,, including both unidentified specimens and those attributed previously to botanical names that are now uncertain. The model’s training images include the vetted Florissant images and all the cleared and x-rayed leaf images described in Wilf et al. 2021. We hope that this tool will stimulate new research into the world-famous Florissant flora, as we work to generalize the algorithms to apply to other fossil sites.</p>
    <p>We are eager to hear from the expert community. Your feedback will help us gauge how many of these classifications are plausible and where further exploration is needed. We look forward to your input in advancing this exciting field!</p>
    <p>The website includes the following features.</p>

    <h4>1. Feedback Table 📊</h4>
    <ul>
        <li>The table displays a comprehensive list of unidentified fossils.</li>
        <li>Each row contains:
          <ul>
              <li>Fossil name (clickable hyperlink)</li>
              <li>Fossil image of the given specimen</li>
              <li>Top five predictions (clickable hyperlink to class concept page)</li>
              <li>Feedback button: We are looking to see what  classifications are “Plausible”, “Impossible”, “Maybe”. To assess our model fitness for this task. Please simply skip over poorly preserved or inapplicable specimens (see Disclaimers below).</li>
          </ul>
        </li>
    </ul>

    <h4>2. Fossil detail website 🔬</h4>

        <p>In this view, you will find details about the Fossil specimen, including its repository number. You can easily find additional metadata for the specimens, including prior identifications, from their filenames (CU- or FLFO- prefix), with these metadata tables kindly provided by Dr. Meyer (see Wilf et al. 2021 for more information about these two image sets): </p>
        <ul>
            <li><a href = "https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank">Florissant CU Metadata </a></li>
            <li><a href = "https://docs.google.com/spreadsheets/d/1o7OIcT5ikbqbk5bJIWYm-jesXnIc5whp/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true" target="_blank">Florissant FLFO Metadata</a></li>
        </ul>
        <p>As well you will find the top 5 family predictions associated with this specimen. The samples from our dataset that are most similar to the provided specimen.</p>
        <p>Finally, you will find the concepts that were utilized by the model in the classification process. These concepts are parts of the images that are useful for family identification through the dataset. In this context, concepts are visual or structural patterns in the specimen that the model uses for classification. These often correspond to diagnostic morphological traits used in traditional taxonomy, such as: Pattern of dentation, leaf venation, symmetry, etc. You can also click on them to explore more details about the concept and other families where the concept is common. </p>

    <h4>3. The Feedback Procedure</h4>
    <p>You can interact with each fossil prediction by:</p>
    <ol>
      <li>For each row you can mark any of the following interactions</li>
      <ul>
        <li>✅ Marking as "Plausible" : In your best judgement, one or multiple of the families proposed can be actually the family of the specimen.</li>
        <li>❌ Marking as "Impossible" : No way! None of the predictions make sense for this specimen. </li>
        <li>🤷‍♀️ Selecting "Maybe" : Actually, not sure, maybe some could be.</li>
      </ul>
      <li>Response Tracking 💾</li>
      <ul>
        <li>Use the "Download Responses" button (bottom right) to save your choices as a JSON file.</li>
        <li><strong>Important:</strong> Download before closing the website to avoid losing responses.</li>
      </ul>
      <li> Resuming Your Work 🔄</li>
      <ul>
        <li>You can resume work using serial numbers during your next visit.</li>
      </ul>
      <li>Sending your feedback: your feedback on any portion of the dataset is greatly appreciated. Feel free to send the downloaded Json file to ivan_felipe_rodriguez@brown.edu</li>
    </ol>

    <h4>Disclaimers</h4>
    
    <p>Please note that while our dataset is extensive, many fossil samples are badly preserved and may lack the detail needed for accurate classification. In addition, although the images were manually filtered several years ago to remove most of them, there remain many images of monocots (which are severely undersampled in the training dataset), reproductive organs (likewise), and non-plant fossils (feathers, fish, and so on). We recommend simply skipping these poorly preserved or inapplicable specimens to ensure more reliable results. Finally, please be aware that the model can only predict families that are in its training dataset, listed here.</p>
    <p><em>We invite you to explore this innovative blend of paleobotany and artificial intelligence, and to join us in refining the art and science of fossil leaf identification! 🍂🌿</em></p>

</div>

</body>
</html>

