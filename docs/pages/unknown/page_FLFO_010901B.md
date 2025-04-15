
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image and Predictions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
        }
        .container {
            max-width: 100%;
            margin: 20px auto;
            padding: 20px;
        }
        h1, h2 {
            text-align: center;
            color: #2c3e50;
        }
        .image-name, .predictions {
            text-align: center;
            margin-bottom: 20px;
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .main-image-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .main-image-container img {
            width: 300px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .concept-card {
            width: 100%; /* Full width of the container */
            max-width: 900px; /* Increased max width */
            padding: 30px; /* More padding for better spacing */
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .concept-container {
            display: flex;
            flex-direction: column;
            gap: 100px;
        }

        .concept-card:hover {
            transform: scale(1.07);
            box-shadow: 0 8px 16px rgba(0,0,0,0.25);
        }

        .concept-images {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
        }

        .concept-images img {
            width: 400px;
            height: 400px;
            object-fit: contain;
            border-radius: 10px;
        }

        .concept-images img:hover {
            transform: scale(1.5);
            transition: transform 0.3s ease;
            box-shadow: 0 8px 16px rgba(0,0,0,0);
        }

        .concept-caption {
            text-align: center;
            font-weight: bold;
            margin-top: 15px;
            width: 100%;
            font-size: 1.2em;
        }

        .predictions a {
            text-decoration: none;
            color: green;
            font-weight: bold;
            transition: color 0.3s ease, transform 0.2s ease;
        }

        .predictions a:hover {
            color: blue;
        }

        .similar-images {
            margin-top: 2em;
            padding: 1em;
            background-color: #f5f5f5;
            border-radius: 8px;
        }

        .similar-images h3 {
            margin-bottom: 1em;
            color: #333;
        }
        .similar-images-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1em;
        }
        .similar-image {
            width: 100%;
            aspect-ratio: 1;
            object-fit: contain;
            border-radius: 4px;
            transition: transform 0.2s;
        }

        .similar-image-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%; /* Matches image width */
        }

        .similar-image:hover {
            transform: scale(1.4);
        }

        .image-caption {
            width: 150px; /* Match image width */
            text-align: center;
            font-size: 0.5em;
            margin-top: 5px;
            word-wrap: break-word; /* Ensures text wraps within width */
            overflow-wrap: break-word; /* Alternative for better compatibility */
        }

        @media (max-width: 768px) {
            .similar-images-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Leaf Fossil and Concept Predictions</h1>
        <div class="image-name">Unidentified Fossil Name: <strong>FLFO_010901B</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank"><em> Viburnaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank"><em> Rosaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank"><em> Celastraceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank"><em> Primulaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank"><em> Rutaceae </em></a>
            </p>
        </div>
        <div class="predictions">
            <h2>Information</h2>
            <p>
                <b>Catalog #</b>: FLFO 10901
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010901B/image.jpg" alt="Fossil Image">
        </div>
        <div class="main-image-container">
            <h3>Similar Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004229.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004229.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004229</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010561B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010561B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010561B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003535A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003535A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003535A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003525.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003525.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_003525</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_002896B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_002896B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_002896B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004768B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004768B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_004768B</div>
                </div>
            </div>
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            <div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20414/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_1_414.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20414/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_414_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 414</em>, relative rank:  1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2081/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_2_81.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2081/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_81_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 81</em>, relative rank:  2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20721/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_3_721.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20721/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_721_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 721</em>, relative rank:  3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_4_382.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_382_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 382</em>, relative rank:  4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20607/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_5_607.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20607/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_607_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 607</em>, relative rank:  5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20752/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_6_752.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20752/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_752_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 752</em>, relative rank:  6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201325/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_7_1325.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201325/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1325_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1325</em>, relative rank:  7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201921/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_8_1921.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201921/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1921_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1921</em>, relative rank:  8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201884/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_9_1884.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201884/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1884_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1884</em>, relative rank:  9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20765/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010901B/concept_10_765.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20765/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_765_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 765</em>, relative rank:  10</div>
            </div>
        </div>
    </div>
</body>
</html>
