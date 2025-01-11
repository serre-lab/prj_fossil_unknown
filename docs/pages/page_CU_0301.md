
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
    <div class="image-name">Image Name: <strong>Image CU_0301</strong></div>
    <div class="predictions">
        Top 5 Predictions: Anacardiaceae, Cupressaceae, Ranunculaceae, Nyssaceae, Myrtaceae
    </div>
    <div class="divider"></div>
    <div class="main-image-container">
        <h2>Main Image</h2>
        <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0301/image.jpg" alt="Fossil Image" style="width: 300px; height: 600px; object-fit: contain;>
    </div>
    <div class="divider"></div>
    <div class="concept-grid">
        <div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20908/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_1_908.png" alt="Concept Image 1">
            </a>
            <div class="concept-caption">concept_1_908.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201366/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_2_1366.png" alt="Concept Image 2">
            </a>
            <div class="concept-caption">concept_2_1366.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20859/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_3_859.png" alt="Concept Image 3">
            </a>
            <div class="concept-caption">concept_3_859.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201308/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_4_1308.png" alt="Concept Image 4">
            </a>
            <div class="concept-caption">concept_4_1308.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20986/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_5_986.png" alt="Concept Image 5">
            </a>
            <div class="concept-caption">concept_5_986.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201388/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_6_1388.png" alt="Concept Image 6">
            </a>
            <div class="concept-caption">concept_6_1388.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20397/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_7_397.png" alt="Concept Image 7">
            </a>
            <div class="concept-caption">concept_7_397.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20458/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_8_458.png" alt="Concept Image 8">
            </a>
            <div class="concept-caption">concept_8_458.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%200/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_9_0.png" alt="Concept Image 9">
            </a>
            <div class="concept-caption">concept_9_0.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20512/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts2/fossil_CU_0301/concept_10_512.png" alt="Concept Image 10">
            </a>
            <div class="concept-caption">concept_10_512.png</div>
        </div>
    </div>
</body>
</html>
