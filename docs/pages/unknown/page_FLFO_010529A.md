
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
        <div class="image-name">Unidentified Fossil Name: <strong>FLFO_010529A</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank"><em> Rosaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank"><em> Fabaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank"><em> Viburnaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank"><em> Anacardiaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank"><em> Ulmaceae </em></a>
            </p>
        </div>
        <div class="predictions">
            <h2>Information</h2>
            <p>
                <b>Catalog #</b>: FLFO 10529
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010529A/image.jpg" alt="Fossil Image">
        </div>
        <div class="main-image-container">
            <h3>Similar Fossil Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010998.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010998.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_010998</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010989A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010989A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_010989A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Prunus_gracilis_Florissant_CU_0821.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Prunus_gracilis_Florissant_CU_0821.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Prunus_gracilis_Florissant_CU_0821</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_006132.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_006132.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Cercocarpus_myricaefolius_Florissant_FLFO_006132</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_011546B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_011546B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Kageneckia_coloradensis_Florissant_FLFO_011546B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_002888A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_002888A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_002888A</div>
                </div>
            </div>

            <h3>Similar Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lauraceae/Lauraceae_Licaria_urceolata_Wolfe_Wolfe_14936b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Lauraceae/Lauraceae_Licaria_urceolata_Wolfe_Wolfe_14936b.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Lauraceae_Licaria_urceolata_Wolfe_Wolfe_14936b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Caprifoliaceae/Caprifoliaceae_Lonicera_oblongifolia_Hickey_Hickey_1340.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Caprifoliaceae/Caprifoliaceae_Lonicera_oblongifolia_Hickey_Hickey_1340.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Caprifoliaceae_Lonicera_oblongifolia_Hickey_Hickey_1340</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Achariaceae/Achariaceae_Hydnocarpus_heterophylla_Wolfe_Wolfe_11262.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Achariaceae/Achariaceae_Hydnocarpus_heterophylla_Wolfe_Wolfe_11262.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Achariaceae_Hydnocarpus_heterophylla_Wolfe_Wolfe_11262</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Pyrola_asarifolia_Wolfe_Wolfe_982.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Ericaceae/Ericaceae_Pyrola_asarifolia_Wolfe_Wolfe_982.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Ericaceae_Pyrola_asarifolia_Wolfe_Wolfe_982</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vivianiaceae/Vivianiaceae_Viviania_crenata_Hickey_Hickey_2579.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Vivianiaceae/Vivianiaceae_Viviania_crenata_Hickey_Hickey_2579.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Vivianiaceae_Viviania_crenata_Hickey_Hickey_2579</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Sphaeralcea_munroana_Wolfe_Wolfe_10487.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Sphaeralcea_munroana_Wolfe_Wolfe_10487.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Malvaceae_Sphaeralcea_munroana_Wolfe_Wolfe_10487</div>
                </div>
            </div>
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            <div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20989/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_1_989.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20989/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_989_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 989</em>, relative rank:  1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201349/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_2_1349.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201349/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1349_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1349</em>, relative rank:  2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201482/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_3_1482.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201482/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1482_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1482</em>, relative rank:  3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20268/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_4_268.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20268/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_268_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 268</em>, relative rank:  4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_5_560.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_560_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 560</em>, relative rank:  5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20561/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_6_561.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20561/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_561_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 561</em>, relative rank:  6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201129/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_7_1129.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201129/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1129_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1129</em>, relative rank:  7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20466/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_8_466.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20466/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_466_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 466</em>, relative rank:  8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201109/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_9_1109.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201109/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1109_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1109</em>, relative rank:  9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201913/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_FLFO_010529A/concept_10_1913.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201913/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1913_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1913</em>, relative rank:  10</div>
            </div>
        </div>
    </div>
</body>
</html>
