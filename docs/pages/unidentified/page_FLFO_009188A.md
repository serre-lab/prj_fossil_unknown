
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
        <div class="image-name">Unidentified Fossil Name: <strong>FLFO_009188A</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank"><em> Rosaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank"><em> Dipterocarpaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank"><em> Fabaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank"><em> Fagaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank"><em> Salicaceae </em></a>
            </p>
        </div>
        <div class="predictions">
            <h2>Information</h2>
            <p>
                <b>Catalog #</b>: FLFO 9188
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/FLFO_009188A.jpg" alt="Fossil Image">
        </div>
        <div class="main-image-container">
            <h3>Similar Fossil Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_009281B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_009281B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Fabaceae_sp_Florissant_FLFO_009281B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Caesalpinites_coloradicus_Florissant_FLFO_004293B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Caesalpinites_coloradicus_Florissant_FLFO_004293B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Caesalpinites_coloradicus_Florissant_FLFO_004293B</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Cercis_parvifolia_Florissant_CU_0233.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Cercis_parvifolia_Florissant_CU_0233.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Cercis_parvifolia_Florissant_CU_0233</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Robinia_lesquereuxi_Florissant_FLFO_003606.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Robinia_lesquereuxi_Florissant_FLFO_003606.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Robinia_lesquereuxi_Florissant_FLFO_003606</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_010964A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_010964A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Fabaceae_sp_Florissant_FLFO_010964A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_010964B.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fabaceae/Fabaceae_Fabaceae_sp_Florissant_FLFO_010964B.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Fabaceae_sp_Florissant_FLFO_010964B</div>
                </div>
            </div>

            <h3>Similar Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Drepananthus_sumatranus_Wing_Wing_276-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Drepananthus_sumatranus_Wing_Wing_276-001.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Annonaceae_Drepananthus_sumatranus_Wing_Wing_276-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cercis_texensis_Axelrod_Axelrod_168.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Cercis_texensis_Axelrod_Axelrod_168.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Cercis_texensis_Axelrod_Axelrod_168</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Trichospermum_richii_Wing_Wing_555-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Trichospermum_richii_Wing_Wing_555-002.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Malvaceae_Trichospermum_richii_Wing_Wing_555-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Heliocarpus_americanus_Wing_Wing_591-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Heliocarpus_americanus_Wing_Wing_591-001.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Malvaceae_Heliocarpus_americanus_Wing_Wing_591-001</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Annona_diversifolia_Hickey_Hickey_284.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Annonaceae/Annonaceae_Annona_diversifolia_Hickey_Hickey_284.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Annonaceae_Annona_diversifolia_Hickey_Hickey_284</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Gunneraceae/Gunneraceae_Gunnera_macrophylla_Hickey_Hickey_6921.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Gunneraceae/Gunneraceae_Gunnera_macrophylla_Hickey_Hickey_6921.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Gunneraceae_Gunnera_macrophylla_Hickey_Hickey_6921</div>
                </div>
            </div>
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            <div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201724/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_1_1724.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201724/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1724_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1724</em>, Relative_rank:  1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201902/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_2_1902.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201902/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1902_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1902</em>, Relative_rank:  2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201562/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_3_1562.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201562/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1562_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1562</em>, Relative_rank:  3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201857/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_4_1857.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201857/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1857_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1857</em>, Relative_rank:  4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20665/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_5_665.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20665/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_665_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 665</em>, Relative_rank:  5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20614/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_6_614.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20614/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_614_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 614</em>, Relative_rank:  6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201651/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_7_1651.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201651/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1651_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1651</em>, Relative_rank:  7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20277/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_8_277.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20277/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_277_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 277</em>, Relative_rank:  8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20606/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_9_606.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20606/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_606_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 606</em>, Relative_rank:  9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201598/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_009188A/concept_10_1598.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201598/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1598_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1598</em>, Relative_rank:  10</div>
            </div>
        </div>
    </div>
</body>
</html>
