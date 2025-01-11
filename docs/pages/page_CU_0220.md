
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image and Predictions</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: #333;
            background-color: #f8f8f8;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2 {
            text-align: center;
            color: #000;
        }
        .image-name {
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
            color: #000;
        }
        .predictions {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            background-color: #fff;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .divider {
            width: 100%;
            margin: 30px auto;
            border-top: 1px solid #ddd;
        }
        .main-image-container {
            text-align: center;
            margin: 30px 0;
        }
        .main-image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .concept-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 0 auto;
        }
        .concept-image {
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .concept-image:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .concept-image img {
            width: 100%;
            height: auto;
            display: block;
        }
        .concept-caption {
            padding: 10px;
            font-size: 14px;
            color: #333;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Image and Concept Predictions</h1>
    <div class="image-name">Image Name: <strong>Image CU_0220</strong></div>
    <div class="predictions">
        Top 5 Predictions: Berberidaceae, Sapindaceae, Myrtaceae, Dryopteridaceae, Betulaceae
    </div>
    <div class="divider"></div>
    <div class="main-image-container">
        <h2>Main Image</h2>
        <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0220/image.jpg" alt="Fossil Image" style="width: 300px; height: 600px; object-fit: contain;>
    </div>
    <div class="divider"></div>
    <div class="concept-grid">
        <div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2021/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_1_21.png" alt="Concept Image 1">
            </a>
            <div class="concept-caption">concept_1_21.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201901/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_2_1901.png" alt="Concept Image 2">
            </a>
            <div class="concept-caption">concept_2_1901.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20615/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_3_615.png" alt="Concept Image 3">
            </a>
            <div class="concept-caption">concept_3_615.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201695/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_4_1695.png" alt="Concept Image 4">
            </a>
            <div class="concept-caption">concept_4_1695.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20618/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_5_618.png" alt="Concept Image 5">
            </a>
            <div class="concept-caption">concept_5_618.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201342/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_6_1342.png" alt="Concept Image 6">
            </a>
            <div class="concept-caption">concept_6_1342.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20850/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_7_850.png" alt="Concept Image 7">
            </a>
            <div class="concept-caption">concept_7_850.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%2048/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_8_48.png" alt="Concept Image 8">
            </a>
            <div class="concept-caption">concept_8_48.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20363/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_9_363.png" alt="Concept Image 9">
            </a>
            <div class="concept-caption">concept_9_363.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201445/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0220/concept_10_1445.png" alt="Concept Image 10">
            </a>
            <div class="concept-caption">concept_10_1445.png</div>
        </div>
    </div>
</body>
</html>
