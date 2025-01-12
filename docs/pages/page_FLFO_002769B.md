
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
            padding: 40px 20px;
        }
        h1, h2 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }
        .image-name {
            font-size: 24px;
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }
        .predictions {
            text-align: center;
            font-size: 18px;
            margin-bottom: 40px;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .divider {
            width: 80%;
            margin: 40px auto;
            border-top: 1px solid #e0e0e0;
        }
        .main-image-container {
            text-align: center;
            margin: 40px 0;
        }
        .main-image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }
        .concept-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin: 0 auto;
        }
        .concept-image {
            background-color: #fff;
            border-radius: 10px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .concept-image:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
        }
        .concept-image img {
            width: 100%;
            height: auto;
            display: block;
        }
        .concept-caption {
            padding: 15px;
            font-size: 16px;
            color: #2c3e50;
            font-weight: 600;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Image and Concept Predictions</h1>
        <div class="image-name">Image Name: <strong>Image FLFO_002769B</strong></div>
        <div class="predictions">
            <h2>Top 5 Predictions</h2>
            <p>Rosaceae, Rhamnaceae, Cupressaceae, Sapindaceae, Meliaceae</p>
        </div>
        <div class="divider"></div>
        <div class="main-image-container">
            <h2>Main Image</h2>
            <img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002769B/image.jpg" alt="Fossil Image" style="width: 300px; height: 600px; object-fit: contain;">
        </div>
        <div class="divider"></div>
        <h2>Concept Images</h2>
        <div class="concept-grid">
            <div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20382/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_1_382.png" alt="Concept Image 1" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_1_382.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20367/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_2_367.png" alt="Concept Image 2" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_2_367.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201338/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_3_1338.png" alt="Concept Image 3" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_3_1338.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201282/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_4_1282.png" alt="Concept Image 4" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_4_1282.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%202022/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_5_2022.png" alt="Concept Image 5" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_5_2022.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201416/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_6_1416.png" alt="Concept Image 6" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_6_1416.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20140/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_7_140.png" alt="Concept Image 7" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_7_140.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201957/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_8_1957.png" alt="Concept Image 8" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_8_1957.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%20898/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_9_898.png" alt="Concept Image 9" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_9_898.png</div>
        </div>
<div class="concept-image">
            <a href="https://fel-thomas.github.io/Leaf-Lens/concepts/Concept%201681/" target="_blank">
                <img src="https://storage.googleapis.com/serrelab/prj_fossils/unknown_fossils_concepts3/fossil_FLFO_002769B/concept_10_1681.png" alt="Concept Image 10" style="width: 300px; height: 600px; object-fit: contain;">
            </a>
            <div class="concept-caption">concept_10_1681.png</div>
        </div>
        </div>
    </div>
</body>
</html>
