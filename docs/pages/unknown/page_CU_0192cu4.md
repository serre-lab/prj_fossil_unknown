
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
        <div class="image-name">Unidentified Fossil Name: <strong>CU_0192cu4</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank"><em> Rosaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank"><em> Fabaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank"><em> Rhamnaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank"><em> Vitaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank"><em> Sapindaceae </em></a>
            </p>
        </div>
        <div class="predictions">
            <h2>Information</h2>
            <p>
                <b>InstPrefix+Catalog #</b>: USNM-40771
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192cu4/image.jpg" alt="Fossil Image">
        </div>
        <div class="main-image-container">
            <h3>Similar Fossil Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_003118.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_003118.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_003118</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_scudderi_Florissant_CU_0187.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_scudderi_Florissant_CU_0187.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Amelanchier_scudderi_Florissant_CU_0187</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_009989B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_009989B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_009989B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_sp_Florissant_FLFO_011484.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Amelanchier_sp_Florissant_FLFO_011484.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Amelanchier_sp_Florissant_FLFO_011484</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_006664A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_006664A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_006664A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_010782A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Rosaceae/Rosaceae_Rosa_sp_Florissant_FLFO_010782A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rosaceae_Rosa_sp_Florissant_FLFO_010782A</div>
                </div>
            </div>

            <h3>Similar Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Meliaceae/Meliaceae_Khaya_grandifoliola_Wolfe_Wolfe_4810a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Meliaceae/Meliaceae_Khaya_grandifoliola_Wolfe_Wolfe_4810a.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Meliaceae_Khaya_grandifoliola_Wolfe_Wolfe_4810a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Sarcopetalum_harveyanum_Wolfe_Wolfe_14525.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Menispermaceae/Menispermaceae_Sarcopetalum_harveyanum_Wolfe_Wolfe_14525.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Menispermaceae_Sarcopetalum_harveyanum_Wolfe_Wolfe_14525</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Capirona_decorticans_Wolfe_Wolfe_12765.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Rubiaceae/Rubiaceae_Capirona_decorticans_Wolfe_Wolfe_12765.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Rubiaceae_Capirona_decorticans_Wolfe_Wolfe_12765</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Hymenaea_oblongifolia_Wolfe_Wolfe_2335a.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Hymenaea_oblongifolia_Wolfe_Wolfe_2335a.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Hymenaea_oblongifolia_Wolfe_Wolfe_2335a</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Ormosia_macrophylla_Wolfe_Wolfe_6430.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Ormosia_macrophylla_Wolfe_Wolfe_6430.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Ormosia_macrophylla_Wolfe_Wolfe_6430</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Phaeanthus_splendens_Wolfe_Wolfe_15495b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Phaeanthus_splendens_Wolfe_Wolfe_15495b.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Annonaceae_Phaeanthus_splendens_Wolfe_Wolfe_15495b</div>
                </div>
            </div>
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            <div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20216/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_1_216.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20216/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_216_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 216</em>, relative rank:  1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_2_382.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_382_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 382</em>, relative rank:  2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20227/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_3_227.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20227/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_227_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 227</em>, relative rank:  3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20226/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_4_226.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20226/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_226_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 226</em>, relative rank:  4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20690/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_5_690.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20690/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_690_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 690</em>, relative rank:  5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201463/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_6_1463.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201463/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1463_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1463</em>, relative rank:  6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201604/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_7_1604.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201604/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1604_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1604</em>, relative rank:  7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201598/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_8_1598.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201598/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1598_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1598</em>, relative rank:  8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_9_560.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20560/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_560_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 560</em>, relative rank:  9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20381/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts4/fossil_CU_0192cu4/concept_10_381.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20381/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_381_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 381</em>, relative rank:  10</div>
            </div>
        </div>
    </div>
</body>
</html>
