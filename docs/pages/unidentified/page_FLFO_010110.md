
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
        <div class="image-name">Unidentified Fossil Name: <strong>FLFO_010110</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank"><em> Fagaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank"><em> Fabaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank"><em> Anacardiaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank"><em> Meliaceae </em></a>,
                <a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank"><em> Ulmaceae </em></a>
            </p>
        </div>
        <div class="predictions">
            <h2>Information</h2>
            <p>
                <b>Catalog #</b>: FLFO 10110
            </p>
        </div>
        <div class="main-image-container">
            <h2>Fossil Sample</h2>
            <img src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Unidentified/FLFO_010110.jpg" alt="Fossil Image">
        </div>
        <div class="main-image-container">
            <h3>Similar Fossil Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_mohavensis_Florissant_CU_0145.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_mohavensis_Florissant_CU_0145.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_mohavensis_Florissant_CU_0145</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_dumosoides_Florissant_CU_0637cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_dumosoides_Florissant_CU_0637cu.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_dumosoides_Florissant_CU_0637cu</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_orbata_Florissant_CU_0376cu.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_orbata_Florissant_CU_0376cu.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_orbata_Florissant_CU_0376cu</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_011054A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_011054A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_011054A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_sp_Florissant_FLFO_003178A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Quercus_sp_Florissant_FLFO_003178A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_sp_Florissant_FLFO_003178A</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_010735A.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Florissant_Fossil_v2.0/Fagaceae/Fagaceae_Fagopsis_longifolia_Florissant_FLFO_010735A.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Fagopsis_longifolia_Florissant_FLFO_010735A</div>
                </div>
            </div>

            <h3>Similar Leaf Specimens</h3>
            <div class="similar-images-grid">
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Erythrina_chiriquensis_Wolfe_Wolfe_16458b.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fabaceae/Fabaceae_Erythrina_chiriquensis_Wolfe_Wolfe_16458b.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fabaceae_Erythrina_chiriquensis_Wolfe_Wolfe_16458b</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_chrysolepis_Axelrod_Axelrod_277.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Quercus_chrysolepis_Axelrod_Axelrod_277.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Quercus_chrysolepis_Axelrod_Axelrod_277</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Guindilia_trinervis_Wing_Wing_614-002.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Guindilia_trinervis_Wing_Wing_614-002.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Sapindaceae_Guindilia_trinervis_Wing_Wing_614-002</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Lithocarpus_speciosa_Axelrod_Axelrod_284.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Fagaceae/Fagaceae_Lithocarpus_speciosa_Axelrod_Axelrod_284.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Fagaceae_Lithocarpus_speciosa_Axelrod_Axelrod_284</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Dilodendron_sipinnetum_Hickey_Hickey_1970.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Sapindaceae/Sapindaceae_Dilodendron_sipinnetum_Hickey_Hickey_1970.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Sapindaceae_Dilodendron_sipinnetum_Hickey_Hickey_1970</div>
                </div>
                <div class="similar-image-container">
                    <a href="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Schoutenia_ovata_Wing_Wing_558-001.jpg" target="_blank"><img class="similar-image" src="https://storage.googleapis.com/serrelab/prj_fossils/2024/Extant_Leaves/Malvaceae/Malvaceae_Schoutenia_ovata_Wing_Wing_558-001.jpg" alt="Similar specimen"></a>
                    <div class="image-caption">Malvaceae_Schoutenia_ovata_Wing_Wing_558-001</div>
                </div>
            </div>
        </div>
        <h2>Concept Images</h2>
        <div class="concept-container">
            <div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201520/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_1_1520.png" alt="Concept Image 1">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201520/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1520_fv.webp" alt="Feature Visualization 1">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1520</em>, Relative_rank:  1</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201723/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_2_1723.png" alt="Concept Image 2">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201723/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1723_fv.webp" alt="Feature Visualization 2">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1723</em>, Relative_rank:  2</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20989/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_3_989.png" alt="Concept Image 3">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20989/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_989_fv.webp" alt="Feature Visualization 3">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 989</em>, Relative_rank:  3</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20776/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_4_776.png" alt="Concept Image 4">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20776/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_776_fv.webp" alt="Feature Visualization 4">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 776</em>, Relative_rank:  4</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201109/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_5_1109.png" alt="Concept Image 5">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201109/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1109_fv.webp" alt="Feature Visualization 5">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1109</em>, Relative_rank:  5</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20618/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_6_618.png" alt="Concept Image 6">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20618/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_618_fv.webp" alt="Feature Visualization 6">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 618</em>, Relative_rank:  6</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%202039/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_7_2039.png" alt="Concept Image 7">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%202039/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_2039_fv.webp" alt="Feature Visualization 7">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 2039</em>, Relative_rank:  7</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201327/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_8_1327.png" alt="Concept Image 8">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201327/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1327_fv.webp" alt="Feature Visualization 8">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1327</em>, Relative_rank:  8</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201299/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_9_1299.png" alt="Concept Image 9">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201299/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1299_fv.webp" alt="Feature Visualization 9">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1299</em>, Relative_rank:  9</div>
            </div>
<div class="concept-card">
                <div class="concept-images">
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201612/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/unidentified_fossils_concepts1/fossil_FLFO_010110/concept_10_1612.png" alt="Concept Image 10">
                    </a>
                    <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201612/" target="_blank">
                        <img src="https://storage.googleapis.com/serrelab/prj_fossils/thomas_sae_compressed/concept_1612_fv.webp" alt="Feature Visualization 10">
                    </a>
                </div>
                <div class="concept-caption"><em style="color:blue;">Concept: 1612</em>, Relative_rank:  10</div>
            </div>
        </div>
    </div>
</body>
</html>
