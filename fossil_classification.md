
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fossil Classification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
        }
        .container {
            width: 90%;
            margin: 20px auto;
            overflow-x: auto;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #2c3e50;
            color: white;
        }
        img {
            width: 100px;
            height: 100px;
            object-fit: contain;
            border-radius: 5px;
        }
        .fixed-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #27ae60;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .fixed-button:hover {
            background: #219150;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Fossil Classification</h1>
    <table>
        <tr>
            <th>Fossil Name</th>
            <th>Fossil Image</th>
            <th>Top 5 Predictions</th>
            <th>Correct</th>
            <th>Incorrect</th>
            <th>Maybe</th>
        </tr>
        
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010221/">FLFO_010221</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010221/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0115/">CU_0115</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0115/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0387cu/">CU_0387cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0387cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002787A/">FLFO_002787A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002787A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010745/">FLFO_010745</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010745/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0484cu/">CU_0484cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0484cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010859A/">FLFO_010859A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010859A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0761cu/">CU_0761cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0761cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010533/">FLFO_010533</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010533/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010163A/">FLFO_010163A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010163A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0814cu/">CU_0814cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0814cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0301cu/">CU_0301cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0301cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004813/">FLFO_004813</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004813/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0803/">CU_0803</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0803/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Garryaceae/" target="_blank">Garryaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002868A/">FLFO_002868A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002868A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005579B/">FLFO_005579B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005579B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003196/">FLFO_003196</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003196/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0270/">CU_0270</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0270/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0812/">CU_0812</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0812/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0761cu1/">CU_0761cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0761cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0771cu/">CU_0771cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0771cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004161B/">FLFO_004161B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004161B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006644B/">FLFO_006644B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006644B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010746/">FLFO_010746</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010746/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010417A/">FLFO_010417A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010417A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0750/">CU_0750</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0750/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Pittosporaceae/" target="_blank">Pittosporaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010826/">FLFO_010826</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010826/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008595/">FLFO_008595</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008595/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0461cu/">CU_0461cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0461cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0796/">CU_0796</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0796/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010038B/">FLFO_010038B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010038B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010176A/">FLFO_010176A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010176A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004436/">FLFO_004436</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004436/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010071B/">FLFO_010071B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010071B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_000857/">FLFO_000857</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_000857/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1367/">CU_1367</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1367/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005584A/">FLFO_005584A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005584A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010662B/">FLFO_010662B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010662B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003180B/">FLFO_003180B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003180B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004706A/">FLFO_004706A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004706A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0620/">CU_0620</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0620/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apiaceae/" target="_blank">Apiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006114B/">FLFO_006114B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006114B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002447A/">FLFO_002447A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002447A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0770cu1/">CU_0770cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0770cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0801/">CU_0801</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0801/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003117/">FLFO_003117</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003117/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011541B/">FLFO_011541B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011541B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002617A/">FLFO_002617A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002617A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0217/">CU_0217</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0217/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003490B/">FLFO_003490B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003490B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006174B/">FLFO_006174B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006174B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010122/">FLFO_010122</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010122/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011147A/">FLFO_011147A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011147A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0894/">CU_0894</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0894/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008599B/">FLFO_008599B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008599B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0206/">CU_0206</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0206/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011522B/">FLFO_011522B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011522B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0489/">CU_0489</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0489/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002769A/">FLFO_002769A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002769A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0761/">CU_0761</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0761/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_11115B/">FLFO_11115B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_11115B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0301/">CU_0301</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0301/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0769cu/">CU_0769cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0769cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003600B/">FLFO_003600B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003600B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011061/">FLFO_011061</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011061/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010738B/">FLFO_010738B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010738B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005768B/">FLFO_005768B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005768B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1359/">CU_1359</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1359/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006046/">FLFO_006046</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006046/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010176B/">FLFO_010176B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010176B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0728/">CU_0728</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0728/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myricaceae/" target="_blank">Myricaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0907/">CU_0907</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0907/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003042B/">FLFO_003042B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003042B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010859B/">FLFO_010859B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010859B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_001080AB/">FLFO_001080AB</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_001080AB/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0359/">CU_0359</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0359/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005579A/">FLFO_005579A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005579A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0386/">CU_0386</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0386/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010824A/">FLFO_010824A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010824A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002682B/">FLFO_002682B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002682B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002799B/">FLFO_002799B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002799B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010521A/">FLFO_010521A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010521A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002361B/">FLFO_002361B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002361B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002826/">FLFO_002826</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002826/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010770B/">FLFO_010770B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010770B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0662cu/">CU_0662cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0662cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0192cu4/">CU_0192cu4</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192cu4/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004161A/">FLFO_004161A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004161A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0074/">CU_0074</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0074/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008586A/">FLFO_008586A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008586A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0797/">CU_0797</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0797/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0157cu/">CU_0157cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0157cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0655cu/">CU_0655cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0655cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004015B/">FLFO_004015B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004015B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004598_2/">FLFO_004598_2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004598_2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0641cu/">CU_0641cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0641cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005788/">FLFO_005788</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005788/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011017/">FLFO_011017</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011017/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0683/">CU_0683</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0683/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010321B 2/">FLFO_010321B 2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010321B 2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011062/">FLFO_011062</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011062/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0730/">CU_0730</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0730/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011121B/">FLFO_011121B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011121B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010877B/">FLFO_010877B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010877B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049A_L1/">FLFO_011049A_L1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049A_L1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010307/">FLFO_010307</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010307/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0512cu/">CU_0512cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0512cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0755/">CU_0755</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0755/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Moraceae/" target="_blank">Moraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0192/">CU_0192</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0731cu/">CU_0731cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0731cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003351B/">FLFO_003351B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003351B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010570B/">FLFO_010570B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010570B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0819/">CU_0819</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0819/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010052B/">FLFO_010052B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010052B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0888/">CU_0888</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0888/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0783cu/">CU_0783cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0783cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Solanaceae/" target="_blank">Solanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0662/">CU_0662</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0662/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003166A/">FLFO_003166A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003166A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010901A/">FLFO_010901A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010901A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0901/">CU_0901</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0901/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010347B/">FLFO_010347B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010347B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0512/">CU_0512</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0512/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0220/">CU_0220</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0220/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008529B/">FLFO_008529B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008529B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Moraceae/" target="_blank">Moraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002447B/">FLFO_002447B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002447B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0118cu/">CU_0118cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0118cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0503/">CU_0503</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0503/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011579/">FLFO_011579</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011579/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004784/">FLFO_004784</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004784/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0631/">CU_0631</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0631/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003005/">FLFO_003005</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003005/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010038A/">FLFO_010038A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010038A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0244/">CU_0244</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0244/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0271/">CU_0271</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0271/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0642/">CU_0642</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0642/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004346A/">FLFO_004346A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004346A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0110/">CU_0110</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0110/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0301cu2/">CU_0301cu2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0301cu2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Moraceae/" target="_blank">Moraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003041A/">FLFO_003041A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003041A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006832B/">FLFO_006832B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006832B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0747/">CU_0747</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0747/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0895/">CU_0895</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0895/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002628A/">FLFO_002628A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002628A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0846cu/">CU_0846cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0846cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Altingiaceae/" target="_blank">Altingiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0716cu1/">CU_0716cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0716cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0904/">CU_0904</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0904/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0386cu/">CU_0386cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0386cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010814A/">FLFO_010814A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010814A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003166B/">FLFO_003166B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003166B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0262/">CU_0262</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0262/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008997A/">FLFO_008997A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008997A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0884/">CU_0884</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0884/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004720A/">FLFO_004720A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004720A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011092/">FLFO_011092</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011092/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010759/">FLFO_010759</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010759/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010770A/">FLFO_010770A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010770A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004442/">FLFO_004442</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004442/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011121A/">FLFO_011121A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011121A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0487/">CU_0487</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0487/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0663cu/">CU_0663cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0663cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0751/">CU_0751</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0751/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004637/">FLFO_004637</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004637/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009788/">FLFO_009788</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009788/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0154cu/">CU_0154cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0154cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0755cu/">CU_0755cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0755cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0084/">CU_0084</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0084/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010011/">FLFO_010011</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010011/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0483/">CU_0483</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0483/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Asteraceae/" target="_blank">Asteraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0154/">CU_0154</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0154/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010540A/">FLFO_010540A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010540A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0118cu1/">CU_0118cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0118cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0762/">CU_0762</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0762/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003260A/">FLFO_003260A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003260A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010315/">FLFO_010315</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010315/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005679/">FLFO_005679</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005679/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011453/">FLFO_011453</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011453/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002500/">FLFO_002500</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002500/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myricaceae/" target="_blank">Myricaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0118cu2/">CU_0118cu2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0118cu2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0087/">CU_0087</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0087/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009686/">FLFO_009686</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009686/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0285/">CU_0285</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0285/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002799A/">FLFO_002799A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002799A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002637B/">FLFO_002637B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002637B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0209/">CU_0209</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0209/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004795/">FLFO_004795</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004795/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0177/">CU_0177</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0177/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Winteraceae/" target="_blank">Winteraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004762B/">FLFO_004762B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004762B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008995A/">FLFO_008995A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008995A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0633/">CU_0633</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0633/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0740/">CU_0740</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0740/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010733B/">FLFO_010733B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010733B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Araliaceae/" target="_blank">Araliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003213/">FLFO_003213</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003213/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010159/">FLFO_010159</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010159/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0202/">CU_0202</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0202/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dilleniaceae/" target="_blank">Dilleniaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0332/">CU_0332</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0332/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003260B/">FLFO_003260B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003260B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003388B/">FLFO_003388B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003388B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010803A/">FLFO_010803A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010803A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011542A/">FLFO_011542A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011542A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002443A/">FLFO_002443A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002443A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010863A/">FLFO_010863A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010863A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006848B/">FLFO_006848B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006848B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002581A/">FLFO_002581A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002581A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0494cu/">CU_0494cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0494cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006733A/">FLFO_006733A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006733A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0332cu/">CU_0332cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0332cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010168B_L2/">FLFO_010168B_L2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010168B_L2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002741A/">FLFO_002741A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002741A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002767B/">FLFO_002767B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002767B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0864/">CU_0864</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0864/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0510cu/">CU_0510cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0510cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Styracaceae/" target="_blank">Styracaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049A_L2/">FLFO_011049A_L2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049A_L2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0479cu/">CU_0479cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0479cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004154A/">FLFO_004154A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004154A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0190cu/">CU_0190cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0190cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010838/">FLFO_010838</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010838/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011361B/">FLFO_011361B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011361B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010863B/">FLFO_010863B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010863B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011454B/">FLFO_011454B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011454B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003110B 2/">FLFO_003110B 2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003110B 2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0489cu2/">CU_0489cu2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0489cu2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0107/">CU_0107</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0107/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0442cu/">CU_0442cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0442cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011036A/">FLFO_011036A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011036A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011426/">FLFO_011426</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011426/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0271cu/">CU_0271cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0271cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0211/">CU_0211</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0211/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0778cu/">CU_0778cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0778cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0900/">CU_0900</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0900/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Aquifoliaceae/" target="_blank">Aquifoliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010529A/">FLFO_010529A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010529A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0164/">CU_0164</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0164/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0756cu/">CU_0756cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0756cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004427/">FLFO_004427</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004427/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011095A/">FLFO_011095A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011095A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005672B/">FLFO_005672B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005672B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011023/">FLFO_011023</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011023/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010901B/">FLFO_010901B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010901B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010584/">FLFO_010584</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010584/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010252A/">FLFO_010252A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010252A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010405/">FLFO_010405</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010405/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002901B/">FLFO_002901B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002901B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010379B/">FLFO_010379B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010379B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049B/">FLFO_011049B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004124B/">FLFO_004124B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004124B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Santalaceae/" target="_blank">Santalaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010809B/">FLFO_010809B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010809B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011336/">FLFO_011336</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011336/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003572B/">FLFO_003572B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003572B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Pittosporaceae/" target="_blank">Pittosporaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004154B/">FLFO_004154B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004154B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010311B/">FLFO_010311B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010311B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006733B/">FLFO_006733B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006733B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010123A/">FLFO_010123A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010123A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0478cu1/">CU_0478cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0478cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0789/">CU_0789</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0789/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004609/">FLFO_004609</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004609/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004603/">FLFO_004603</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004603/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0657/">CU_0657</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0657/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009708A/">FLFO_009708A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009708A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004565A/">FLFO_004565A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004565A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010321B/">FLFO_010321B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010321B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0410/">CU_0410</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0410/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Staphyleaceae/" target="_blank">Staphyleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Actinidiaceae/" target="_blank">Actinidiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004015A/">FLFO_004015A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004015A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0662cpt/">CU_0662cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0662cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0830/">CU_0830</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0830/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011520A/">FLFO_011520A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011520A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006114A/">FLFO_006114A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006114A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003514/">FLFO_003514</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003514/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006872B/">FLFO_006872B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006872B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0789cu/">CU_0789cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0789cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0740cu/">CU_0740cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0740cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0440cu/">CU_0440cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0440cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0747cu1/">CU_0747cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0747cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0619/">CU_0619</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0619/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0820cu1/">CU_0820cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0820cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0846/">CU_0846</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0846/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Altingiaceae/" target="_blank">Altingiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0906/">CU_0906</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0906/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0783/">CU_0783</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0783/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0746cu1/">CU_0746cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0746cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011096B/">FLFO_011096B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011096B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_000126/">FLFO_000126</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_000126/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010973B/">FLFO_010973B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010973B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0780/">CU_0780</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0780/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004600/">FLFO_004600</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004600/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049A/">FLFO_011049A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003110A/">FLFO_003110A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003110A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010576A/">FLFO_010576A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010576A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003572A/">FLFO_003572A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003572A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_001797A/">FLFO_001797A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_001797A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002438/">FLFO_002438</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002438/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004597/">FLFO_004597</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004597/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004895A/">FLFO_004895A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004895A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006692/">FLFO_006692</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006692/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006146/">FLFO_006146</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006146/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004720B/">FLFO_004720B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004720B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0332cu-2/">CU_0332cu-2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0332cu-2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0652cu/">CU_0652cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0652cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011094B/">FLFO_011094B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011094B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002489A/">FLFO_002489A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002489A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0801cu/">CU_0801cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0801cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010262B/">FLFO_010262B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010262B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008571A/">FLFO_008571A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008571A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0657cu/">CU_0657cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0657cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011130/">FLFO_011130</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011130/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0336cpt/">CU_0336cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0336cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006912B/">FLFO_006912B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006912B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0739cu/">CU_0739cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0739cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010168B_L1/">FLFO_010168B_L1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010168B_L1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003188/">FLFO_003188</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003188/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0833/">CU_0833</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0833/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyctaginaceae/" target="_blank">Nyctaginaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Opiliaceae/" target="_blank">Opiliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006940A/">FLFO_006940A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006940A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0246/">CU_0246</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0246/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002581B/">FLFO_002581B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002581B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0815/">CU_0815</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0815/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010311A/">FLFO_010311A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010311A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004935/">FLFO_004935</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004935/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004742A/">FLFO_004742A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004742A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0179/">CU_0179</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0179/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011745/">FLFO_011745</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011745/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008513/">FLFO_008513</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008513/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003990A/">FLFO_003990A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003990A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0721/">CU_0721</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0721/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010028 2/">FLFO_010028 2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010028 2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004794/">FLFO_004794</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004794/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002786B/">FLFO_002786B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002786B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0494/">CU_0494</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0494/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ranunculaceae/" target="_blank">Ranunculaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0513cu/">CU_0513cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0513cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010576B/">FLFO_010576B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010576B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1033cu/">CU_1033cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1033cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0833cu1/">CU_0833cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0833cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004346B/">FLFO_004346B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004346B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011199B/">FLFO_011199B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011199B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myristicaceae/" target="_blank">Myristicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apiaceae/" target="_blank">Apiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004895B/">FLFO_004895B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004895B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011094A/">FLFO_011094A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011094A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008972B/">FLFO_008972B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008972B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0244cu/">CU_0244cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0244cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003350B/">FLFO_003350B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003350B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011450B/">FLFO_011450B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011450B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006502B_1/">FLFO_006502B_1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006502B_1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Calophyllaceae/" target="_blank">Calophyllaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002444B/">FLFO_002444B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002444B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011655/">FLFO_011655</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011655/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006174A/">FLFO_006174A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006174A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Moraceae/" target="_blank">Moraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0118/">CU_0118</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0118/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008586B/">FLFO_008586B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008586B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002740B/">FLFO_002740B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002740B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003351A/">FLFO_003351A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003351A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006632B/">FLFO_006632B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006632B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Schisandraceae/" target="_blank">Schisandraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0814/">CU_0814</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0814/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003651/">FLFO_003651</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003651/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004844/">FLFO_004844</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004844/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002483/">FLFO_002483</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002483/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008564B/">FLFO_008564B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008564B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_000888/">FLFO_000888</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_000888/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0073/">CU_0073</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0073/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apiaceae/" target="_blank">Apiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009791A/">FLFO_009791A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009791A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006961B/">FLFO_006961B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006961B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0673cu/">CU_0673cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0673cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010424B/">FLFO_010424B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010424B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011691/">FLFO_011691</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011691/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049B_L1/">FLFO_011049B_L1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049B_L1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0772/">CU_0772</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0772/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011100B/">FLFO_011100B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011100B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008968A/">FLFO_008968A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008968A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003952B/">FLFO_003952B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003952B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003350A/">FLFO_003350A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003350A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0754cu/">CU_0754cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0754cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003234/">FLFO_003234</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003234/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0741cu1/">CU_0741cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0741cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011658/">FLFO_011658</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011658/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0798cu/">CU_0798cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0798cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005650/">FLFO_005650</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005650/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0882/">CU_0882</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0882/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003551/">FLFO_003551</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003551/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Combretaceae/" target="_blank">Combretaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0818/">CU_0818</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0818/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005677B/">FLFO_005677B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005677B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008529A/">FLFO_008529A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008529A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0726/">CU_0726</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0726/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011087A/">FLFO_011087A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011087A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0503cu/">CU_0503cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0503cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010071A/">FLFO_010071A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010071A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0231cu1/">CU_0231cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0231cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0742/">CU_0742</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0742/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002767A/">FLFO_002767A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002767A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010790B/">FLFO_010790B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010790B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010198A/">FLFO_010198A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010198A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myricaceae/" target="_blank">Myricaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003231B/">FLFO_003231B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003231B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010744A/">FLFO_010744A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010744A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0393cu/">CU_0393cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0393cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003083/">FLFO_003083</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003083/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010252B/">FLFO_010252B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010252B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010052A/">FLFO_010052A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010052A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002769B/">FLFO_002769B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002769B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0513cu2/">CU_0513cu2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0513cu2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0504/">CU_0504</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0504/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010197/">FLFO_010197</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010197/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011511/">FLFO_011511</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011511/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0830cu/">CU_0830cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0830cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010529B/">FLFO_010529B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010529B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010656B/">FLFO_010656B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010656B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003388A/">FLFO_003388A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003388A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0207/">CU_0207</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0207/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010790A/">FLFO_010790A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010790A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008511B/">FLFO_008511B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008511B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0769cu1/">CU_0769cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0769cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010459B/">FLFO_010459B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010459B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006078/">FLFO_006078</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006078/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010028/">FLFO_010028</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010028/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011235B/">FLFO_011235B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011235B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0327/">CU_0327</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0327/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003680A/">FLFO_003680A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003680A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006912A/">FLFO_006912A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006912A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0491cu/">CU_0491cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0491cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010656A/">FLFO_010656A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010656A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002879A/">FLFO_002879A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002879A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0820/">CU_0820</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0820/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0510/">CU_0510</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0510/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0192cu1/">CU_0192cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0197/">CU_0197</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0197/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004929/">FLFO_004929</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004929/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011029/">FLFO_011029</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011029/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004260/">FLFO_004260</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004260/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003301A/">FLFO_003301A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003301A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0817cu/">CU_0817cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0817cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003600A/">FLFO_003600A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003600A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0111cu1/">CU_0111cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0111cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002901A/">FLFO_002901A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002901A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008538B/">FLFO_008538B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008538B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0072cu/">CU_0072cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0072cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0401cu/">CU_0401cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0401cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011305/">FLFO_011305</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011305/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006644A/">FLFO_006644A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006644A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0441/">CU_0441</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0441/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011502A/">FLFO_011502A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011502A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0329cu/">CU_0329cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0329cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0489cu/">CU_0489cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0489cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0805/">CU_0805</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0805/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006832A/">FLFO_006832A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006832A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008558A/">FLFO_008558A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008558A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008538A/">FLFO_008538A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008538A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003492B/">FLFO_003492B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003492B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011100A/">FLFO_011100A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011100A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002361A/">FLFO_002361A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002361A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0189/">CU_0189</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0189/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002786A/">FLFO_002786A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002786A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0454/">CU_0454</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0454/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011087B/">FLFO_011087B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011087B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0654/">CU_0654</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0654/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0854/">CU_0854</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0854/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0729/">CU_0729</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0729/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002420B/">FLFO_002420B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002420B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oxalidaceae/" target="_blank">Oxalidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002702/">FLFO_002702</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002702/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008590B/">FLFO_008590B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008590B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008995B/">FLFO_008995B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008995B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1032/">CU_1032</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1032/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0741/">CU_0741</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0741/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0241/">CU_0241</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0241/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004707B/">FLFO_004707B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004707B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0770/">CU_0770</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0770/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0753cu/">CU_0753cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0753cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0896/">CU_0896</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0896/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0454cu/">CU_0454cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0454cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010888/">FLFO_010888</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010888/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0513cu1/">CU_0513cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0513cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0741cu/">CU_0741cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0741cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0329/">CU_0329</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0329/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0901cpt/">CU_0901cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0901cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010650B/">FLFO_010650B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010650B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003258/">FLFO_003258</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003258/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0686/">CU_0686</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0686/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0409/">CU_0409</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0409/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0122/">CU_0122</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0122/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003490A/">FLFO_003490A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003490A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ebenaceae/" target="_blank">Ebenaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002926A/">FLFO_002926A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002926A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010329A/">FLFO_010329A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010329A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0513/">CU_0513</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0513/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002597/">FLFO_002597</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002597/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0198cpt/">CU_0198cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0198cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0440/">CU_0440</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0440/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010463A/">FLFO_010463A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010463A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010519A/">FLFO_010519A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010519A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010163B/">FLFO_010163B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010163B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0486/">CU_0486</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0486/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009675/">FLFO_009675</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009675/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006649/">FLFO_006649</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006649/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002728/">FLFO_002728</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002728/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006502A_1/">FLFO_006502A_1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006502A_1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1364/">CU_1364</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1364/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0902cu/">CU_0902cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0902cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011019A/">FLFO_011019A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011019A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0307/">CU_0307</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0307/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0687/">CU_0687</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0687/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009259/">FLFO_009259</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009259/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0448cu/">CU_0448cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0448cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0118cu3/">CU_0118cu3</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0118cu3/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003420B/">FLFO_003420B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003420B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0754/">CU_0754</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0754/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010423A/">FLFO_010423A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010423A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011361A/">FLFO_011361A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011361A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0745/">CU_0745</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0745/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006940B/">FLFO_006940B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006940B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010680B/">FLFO_010680B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010680B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0641/">CU_0641</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0641/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0744cu/">CU_0744cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0744cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005584B/">FLFO_005584B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005584B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011133A/">FLFO_011133A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011133A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010409A/">FLFO_010409A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010409A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002682A/">FLFO_002682A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002682A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0461/">CU_0461</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0461/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011133B/">FLFO_011133B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011133B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011147B/">FLFO_011147B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011147B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Aquifoliaceae/" target="_blank">Aquifoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003177B/">FLFO_003177B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003177B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010562B/">FLFO_010562B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010562B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008967/">FLFO_008967</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008967/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010168B_L3/">FLFO_010168B_L3</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010168B_L3/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0279/">CU_0279</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0279/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010806A/">FLFO_010806A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010806A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002741B/">FLFO_002741B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002741B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010459A/">FLFO_010459A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010459A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010897B/">FLFO_010897B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010897B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006837B/">FLFO_006837B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006837B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003152/">FLFO_003152</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003152/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010137/">FLFO_010137</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010137/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003175A/">FLFO_003175A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003175A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0809/">CU_0809</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0809/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011502B/">FLFO_011502B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011502B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010002A/">FLFO_010002A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010002A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0591cu/">CU_0591cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0591cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002869B/">FLFO_002869B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002869B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010699A/">FLFO_010699A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010699A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0760cu1/">CU_0760cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0760cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cunoniaceae/" target="_blank">Cunoniaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0194cpt/">CU_0194cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0194cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0393/">CU_0393</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0393/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003240/">FLFO_003240</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003240/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011080A/">FLFO_011080A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011080A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006632A/">FLFO_006632A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006632A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0673/">CU_0673</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0673/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0833cu/">CU_0833cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0833cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004124A/">FLFO_004124A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004124A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005677A/">FLFO_005677A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005677A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011199A/">FLFO_011199A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011199A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011115A/">FLFO_011115A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011115A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003952A/">FLFO_003952A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003952A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0746cu/">CU_0746cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0746cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0301cu1/">CU_0301cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0301cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0512cu1/">CU_0512cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0512cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0410cu1/">CU_0410cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0410cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0511/">CU_0511</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0511/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010308B/">FLFO_010308B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010308B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008571B/">FLFO_008571B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008571B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004443B/">FLFO_004443B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004443B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lamiaceae/" target="_blank">Lamiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004708B/">FLFO_004708B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004708B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010662A/">FLFO_010662A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010662A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004519A/">FLFO_004519A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004519A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010562A/">FLFO_010562A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010562A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002703/">FLFO_002703</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002703/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0820cu/">CU_0820cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0820cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010650A/">FLFO_010650A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010650A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009029B/">FLFO_009029B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009029B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004838A/">FLFO_004838A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004838A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010738A/">FLFO_010738A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010738A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010780A/">FLFO_010780A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010780A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011019B/">FLFO_011019B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011019B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010734A/">FLFO_010734A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010734A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0752/">CU_0752</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0752/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011025/">FLFO_011025</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011025/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003311B/">FLFO_003311B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003311B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0360/">CU_0360</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0360/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sarcolaenaceae/" target="_blank">Sarcolaenaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0180/">CU_0180</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0180/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011518/">FLFO_011518</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011518/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010897A/">FLFO_010897A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010897A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010045/">FLFO_010045</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010045/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009286/">FLFO_009286</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009286/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Magnoliaceae/" target="_blank">Magnoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Olacaceae/" target="_blank">Olacaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002623B/">FLFO_002623B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002623B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005678/">FLFO_005678</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005678/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008558B/">FLFO_008558B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008558B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009680/">FLFO_009680</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009680/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010029/">FLFO_010029</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010029/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010993B/">FLFO_010993B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010993B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009859/">FLFO_009859</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009859/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010031/">FLFO_010031</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010031/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010070A Cyperacites lacustris/">FLFO_010070A Cyperacites lacustris</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010070A Cyperacites lacustris/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004519B/">FLFO_004519B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004519B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010734B/">FLFO_010734B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010734B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006872A/">FLFO_006872A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006872A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010415A/">FLFO_010415A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010415A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0448/">CU_0448</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0448/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003179B/">FLFO_003179B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003179B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0198pt/">CU_0198pt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0198pt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010052B 2/">FLFO_010052B 2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010052B 2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003180A/">FLFO_003180A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003180A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapotaceae/" target="_blank">Sapotaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0808/">CU_0808</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0808/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Paracryphiaceae/" target="_blank">Paracryphiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002868B/">FLFO_002868B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002868B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002676B/">FLFO_002676B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002676B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010347A/">FLFO_010347A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010347A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002743A/">FLFO_002743A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002743A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006651A/">FLFO_006651A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006651A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004608/">FLFO_004608</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004608/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008564A/">FLFO_008564A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008564A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0810/">CU_0810</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0810/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Altingiaceae/" target="_blank">Altingiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011181/">FLFO_011181</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011181/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002709/">FLFO_002709</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002709/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0601cu/">CU_0601cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0601cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0192cu3/">CU_0192cu3</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192cu3/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0214/">CU_0214</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0214/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0652/">CU_0652</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0652/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0247/">CU_0247</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0247/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0336cu/">CU_0336cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0336cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004708A/">FLFO_004708A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004708A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Solanaceae/" target="_blank">Solanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011520B/">FLFO_011520B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011520B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010680A/">FLFO_010680A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010680A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002743B/">FLFO_002743B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002743B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008599A/">FLFO_008599A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008599A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010861/">FLFO_010861</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010861/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0189p+cpt/">CU_0189p+cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0189p+cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003177A/">FLFO_003177A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003177A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011080B/">FLFO_011080B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011080B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0336/">CU_0336</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0336/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polemoniaceae/" target="_blank">Polemoniaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0265/">CU_0265</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0265/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003041B/">FLFO_003041B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003041B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0716cu/">CU_0716cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0716cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Aquifoliaceae/" target="_blank">Aquifoliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010577/">FLFO_010577</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010577/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0111/">CU_0111</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0111/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011562/">FLFO_011562</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011562/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010198B/">FLFO_010198B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010198B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Paracryphiaceae/" target="_blank">Paracryphiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hypericaceae/" target="_blank">Hypericaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0115cu/">CU_0115cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0115cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006653B/">FLFO_006653B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006653B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010683B/">FLFO_010683B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010683B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0459/">CU_0459</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0459/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0674/">CU_0674</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0674/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049B_L2/">FLFO_011049B_L2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049B_L2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004932/">FLFO_004932</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004932/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004235A/">FLFO_004235A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004235A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010016A/">FLFO_010016A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010016A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010744B/">FLFO_010744B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010744B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0479/">CU_0479</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0479/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011680/">FLFO_011680</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011680/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Melastomataceae/" target="_blank">Melastomataceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002456/">FLFO_002456</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002456/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0810cu/">CU_0810cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0810cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hydrangeaceae/" target="_blank">Hydrangeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_001797B/">FLFO_001797B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_001797B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Gnetaceae/" target="_blank">Gnetaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0484cu1/">CU_0484cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0484cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002879B/">FLFO_002879B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002879B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0441cu1/">CU_0441cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0441cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0484/">CU_0484</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0484/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lamiaceae/" target="_blank">Lamiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0729cu/">CU_0729cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0729cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002637A/">FLFO_002637A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002637A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0478/">CU_0478</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0478/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010383B/">FLFO_010383B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010383B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0199cu/">CU_0199cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0199cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011450A/">FLFO_011450A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011450A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011051A/">FLFO_011051A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011051A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004762A/">FLFO_004762A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004762A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011020A/">FLFO_011020A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011020A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006606B/">FLFO_006606B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006606B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0285cu/">CU_0285cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0285cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0074cu/">CU_0074cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0074cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011542B/">FLFO_011542B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011542B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010685A/">FLFO_010685A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010685A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003143/">FLFO_003143</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003143/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011096A/">FLFO_011096A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011096A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0490cu/">CU_0490cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0490cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0401/">CU_0401</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0401/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008989A/">FLFO_008989A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008989A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Pittosporaceae/" target="_blank">Pittosporaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0687cu/">CU_0687cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0687cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lamiaceae/" target="_blank">Lamiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010685B/">FLFO_010685B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010685B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010423B/">FLFO_010423B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010423B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004581/">FLFO_004581</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004581/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010824B/">FLFO_010824B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010824B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0215/">CU_0215</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0215/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006502B/">FLFO_006502B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006502B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apocynaceae/" target="_blank">Apocynaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Calophyllaceae/" target="_blank">Calophyllaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003070/">FLFO_003070</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003070/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002639B/">FLFO_002639B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002639B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010321A/">FLFO_010321A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010321A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010383A/">FLFO_010383A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010383A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003438/">FLFO_003438</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003438/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009861A/">FLFO_009861A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009861A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002683A/">FLFO_002683A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002683A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Actinidiaceae/" target="_blank">Actinidiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003179A/">FLFO_003179A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003179A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010753B/">FLFO_010753B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010753B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003665/">FLFO_003665</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003665/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002623A/">FLFO_002623A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002623A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0442/">CU_0442</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0442/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010083/">FLFO_010083</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010083/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0685/">CU_0685</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0685/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Pittosporaceae/" target="_blank">Pittosporaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008590A/">FLFO_008590A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008590A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0747cu/">CU_0747cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0747cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0199/">CU_0199</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0199/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003999/">FLFO_003999</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003999/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002444A/">FLFO_002444A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002444A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006651B/">FLFO_006651B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006651B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002420A/">FLFO_002420A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002420A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004836/">FLFO_004836</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004836/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0217cu/">CU_0217cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0217cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010269/">FLFO_010269</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010269/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010877A/">FLFO_010877A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010877A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Schisandraceae/" target="_blank">Schisandraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0494cu1/">CU_0494cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0494cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cornaceae/" target="_blank">Cornaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002740A/">FLFO_002740A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002740A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002443B/">FLFO_002443B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002443B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008505/">FLFO_008505</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008505/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0642cu/">CU_0642cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0642cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010578B/">FLFO_010578B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010578B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011051B/">FLFO_011051B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011051B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0289/">CU_0289</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0289/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ochnaceae/" target="_blank">Ochnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Marantaceae/" target="_blank">Marantaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Chloranthaceae/" target="_blank">Chloranthaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011235A/">FLFO_011235A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011235A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010753A/">FLFO_010753A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010753A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003231A/">FLFO_003231A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003231A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010683A/">FLFO_010683A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010683A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011454A/">FLFO_011454A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011454A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0511cu/">CU_0511cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0511cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010570A/">FLFO_010570A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010570A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010002B/">FLFO_010002B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010002B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010623/">FLFO_010623</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010623/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010424A/">FLFO_010424A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010424A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006653A/">FLFO_006653A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006653A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003311A/">FLFO_003311A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003311A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Olacaceae/" target="_blank">Olacaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011561/">FLFO_011561</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011561/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011541A/">FLFO_011541A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011541A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008989B/">FLFO_008989B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008989B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nyssaceae/" target="_blank">Nyssaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002617B/">FLFO_002617B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002617B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004706B/">FLFO_004706B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004706B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002683B/">FLFO_002683B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002683B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010806B/">FLFO_010806B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010806B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0360cu/">CU_0360cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0360cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dilleniaceae/" target="_blank">Dilleniaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sarcolaenaceae/" target="_blank">Sarcolaenaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004543/">FLFO_004543</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004543/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0746/">CU_0746</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0746/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011059/">FLFO_011059</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011059/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006734B/">FLFO_006734B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006734B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0491/">CU_0491</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0491/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0756/">CU_0756</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0756/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0744/">CU_0744</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0744/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0327cu/">CU_0327cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0327cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Schisandraceae/" target="_blank">Schisandraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0731/">CU_0731</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0731/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Elaeocarpaceae/" target="_blank">Elaeocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0315cptcu1/">CU_0315cptcu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0315cptcu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0742cu/">CU_0742cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0742cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010379A/">FLFO_010379A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010379A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009610A/">FLFO_009610A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009610A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006848A/">FLFO_006848A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006848A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011095B/">FLFO_011095B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011095B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0693/">CU_0693</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0693/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0166/">CU_0166</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0166/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0739/">CU_0739</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0739/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0817/">CU_0817</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0817/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003810/">FLFO_003810</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003810/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0771/">CU_0771</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0771/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011652A/">FLFO_011652A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011652A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010417B/">FLFO_010417B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010417B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010867/">FLFO_010867</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010867/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008997B/">FLFO_008997B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008997B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004565B/">FLFO_004565B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004565B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010803B/">FLFO_010803B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010803B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1374/">CU_1374</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1374/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010271_L1/">FLFO_010271_L1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010271_L1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0315/">CU_0315</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0315/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004579/">FLFO_004579</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004579/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0185/">CU_0185</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0185/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0214cu/">CU_0214cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0214cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0483cu/">CU_0483cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0483cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003042A/">FLFO_003042A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003042A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003175B/">FLFO_003175B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003175B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0907cu/">CU_0907cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0907cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004235B/">FLFO_004235B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004235B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010993A/">FLFO_010993A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010993A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010397/">FLFO_010397</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010397/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010321A 2/">FLFO_010321A 2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010321A 2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0769/">CU_0769</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0769/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003990B/">FLFO_003990B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003990B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0157cu1/">CU_0157cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0157cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010805/">FLFO_010805</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010805/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004623/">FLFO_004623</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004623/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011036B/">FLFO_011036B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011036B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010809A/">FLFO_010809A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010809A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0336cptcu/">CU_0336cptcu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0336cptcu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0759/">CU_0759</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0759/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Zygophyllaceae/" target="_blank">Zygophyllaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006606A/">FLFO_006606A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006606A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0895cu/">CU_0895cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0895cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008980/">FLFO_008980</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008980/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006937/">FLFO_006937</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006937/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0760/">CU_0760</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0760/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0261/">CU_0261</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0261/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0591/">CU_0591</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0591/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004598_1/">FLFO_004598_1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004598_1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0655/">CU_0655</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0655/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0905/">CU_0905</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0905/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003597A/">FLFO_003597A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003597A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003233/">FLFO_003233</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003233/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006932/">FLFO_006932</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006932/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004692/">FLFO_004692</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004692/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006961A/">FLFO_006961A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006961A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006939A/">FLFO_006939A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006939A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009976A/">FLFO_009976A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009976A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002628B/">FLFO_002628B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002628B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011020B/">FLFO_011020B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011020B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006837A/">FLFO_006837A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006837A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010540B/">FLFO_010540B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010540B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002833/">FLFO_002833</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002833/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002676A/">FLFO_002676A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002676A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008511A/">FLFO_008511A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008511A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011515A/">FLFO_011515A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011515A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004422/">FLFO_004422</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004422/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010699B/">FLFO_010699B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010699B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0190/">CU_0190</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0190/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010463B/">FLFO_010463B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010463B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_001055/">FLFO_001055</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_001055/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Euphorbiaceae/" target="_blank">Euphorbiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009708B/">FLFO_009708B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009708B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009029A/">FLFO_009029A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009029A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0503cpt/">CU_0503cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0503cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Styracaceae/" target="_blank">Styracaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011367/">FLFO_011367</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011367/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002639A/">FLFO_002639A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002639A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003106/">FLFO_003106</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003106/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002660/">FLFO_002660</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002660/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0721cu/">CU_0721cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0721cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0111cu/">CU_0111cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0111cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0194/">CU_0194</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0194/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004742B/">FLFO_004742B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004742B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003680B/">FLFO_003680B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003680B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0315cpt/">CU_0315cpt</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0315cpt/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0490/">CU_0490</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0490/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003172/">FLFO_003172</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003172/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0656/">CU_0656</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0656/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cannabaceae/" target="_blank">Cannabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004455/">FLFO_004455</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004455/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lamiaceae/" target="_blank">Lamiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Staphyleaceae/" target="_blank">Staphyleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Actinidiaceae/" target="_blank">Actinidiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0486cu/">CU_0486cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0486cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Moraceae/" target="_blank">Moraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008968B/">FLFO_008968B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008968B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010742B/">FLFO_010742B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010742B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008972A/">FLFO_008972A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008972A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Apiaceae/" target="_blank">Apiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004761A/">FLFO_004761A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004761A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0215cu/">CU_0215cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0215cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0076/">CU_0076</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0076/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rubiaceae/" target="_blank">Rubiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0315cptcu/">CU_0315cptcu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0315cptcu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0654cu/">CU_0654cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0654cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010097B/">FLFO_010097B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010097B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0410cu/">CU_0410cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0410cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004611/">FLFO_004611</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004611/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Burseraceae/" target="_blank">Burseraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010955/">FLFO_010955</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010955/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003597B/">FLFO_003597B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003597B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004321/">FLFO_004321</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004321/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009610B/">FLFO_009610B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009610B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Nothofagaceae/" target="_blank">Nothofagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004545/">FLFO_004545</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004545/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004550A/">FLFO_004550A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004550A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011522A/">FLFO_011522A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011522A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011652B/">FLFO_011652B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011652B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010578A/">FLFO_010578A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010578A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0743cu/">CU_0743cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0743cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002926B/">FLFO_002926B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002926B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0743/">CU_0743</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0743/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0478cu/">CU_0478cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0478cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0156/">CU_0156</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0156/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_1033/">CU_1033</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_1033/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004930/">FLFO_004930</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004930/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011081A/">FLFO_011081A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011081A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0312/">CU_0312</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0312/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010742A/">FLFO_010742A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010742A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0485/">CU_0485</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0485/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lamiaceae/" target="_blank">Lamiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002787B/">FLFO_002787B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002787B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009791B/">FLFO_009791B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009791B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0674cu/">CU_0674cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0674cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010780B/">FLFO_010780B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010780B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0778/">CU_0778</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0778/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004707A/">FLFO_004707A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004707A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010016B/">FLFO_010016B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010016B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010415B/">FLFO_010415B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010415B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011049B_L3/">FLFO_011049B_L3</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011049B_L3/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0745cu/">CU_0745cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0745cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010168A_L3/">FLFO_010168A_L3</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010168A_L3/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010123B/">FLFO_010123B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010123B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009861B/">FLFO_009861B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009861B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0601/">CU_0601</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0601/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003301B/">FLFO_003301B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003301B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006232/">FLFO_006232</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006232/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0409cu/">CU_0409cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0409cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003354/">FLFO_003354</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003354/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0752cu1/">CU_0752cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0752cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Menispermaceae/" target="_blank">Menispermaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Passifloraceae/" target="_blank">Passifloraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008724/">FLFO_008724</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008724/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0198/">CU_0198</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0198/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cornaceae/" target="_blank">Cornaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0900cu/">CU_0900cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0900cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0441cu/">CU_0441cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0441cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003513/">FLFO_003513</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003513/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0082/">CU_0082</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0082/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010774/">FLFO_010774</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010774/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010070B Cyperacites lacustris/">FLFO_010070B Cyperacites lacustris</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010070B Cyperacites lacustris/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003492A/">FLFO_003492A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003492A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0336cu1/">CU_0336cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0336cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011081B/">FLFO_011081B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011081B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003110B/">FLFO_003110B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003110B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0231/">CU_0231</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0231/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010521B/">FLFO_010521B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010521B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004838B/">FLFO_004838B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004838B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_000094/">FLFO_000094</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_000094/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Connaraceae/" target="_blank">Connaraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0815cu/">CU_0815cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0815cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Oleaceae/" target="_blank">Oleaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0459cu/">CU_0459cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0459cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010271_L2/">FLFO_010271_L2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010271_L2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0171cu/">CU_0171cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0171cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006624/">FLFO_006624</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006624/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004550B/">FLFO_004550B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004550B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010409B/">FLFO_010409B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010409B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010733A/">FLFO_010733A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010733A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004443A/">FLFO_004443A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004443A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0231cu/">CU_0231cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0231cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005768A/">FLFO_005768A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005768A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0147/">CU_0147</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0147/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0281/">CU_0281</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0281/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_004540/">FLFO_004540</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_004540/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0504cu/">CU_0504cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0504cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008550/">FLFO_008550</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008550/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_003420A/">FLFO_003420A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_003420A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0387/">CU_0387</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0387/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Hamamelidaceae/" target="_blank">Hamamelidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_000095/">FLFO_000095</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_000095/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Dipterocarpaceae/" target="_blank">Dipterocarpaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0157/">CU_0157</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0157/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002638A/">FLFO_002638A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002638A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Staphyleaceae/" target="_blank">Staphyleaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_009976B/">FLFO_009976B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_009976B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Urticaceae/" target="_blank">Urticaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Icacinaceae/" target="_blank">Icacinaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010814B/">FLFO_010814B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010814B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0716/">CU_0716</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0716/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010262A/">FLFO_010262A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010262A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Cornaceae/" target="_blank">Cornaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0753/">CU_0753</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0753/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Phyllanthaceae/" target="_blank">Phyllanthaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0770cu/">CU_0770cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0770cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Celastraceae/" target="_blank">Celastraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Polygonaceae/" target="_blank">Polygonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0171/">CU_0171</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0171/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010519B/">FLFO_010519B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010519B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0743cu1/">CU_0743cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0743cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ericaceae/" target="_blank">Ericaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0122cu/">CU_0122cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0122cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0072/">CU_0072</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0072/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002489B/">FLFO_002489B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002489B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011515B/">FLFO_011515B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011515B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Juglandaceae/" target="_blank">Juglandaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Vitaceae/" target="_blank">Vitaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008977/">FLFO_008977</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008977/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0693cu/">CU_0693cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0693cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006734A/">FLFO_006734A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006734A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sabiaceae/" target="_blank">Sabiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0192cu2/">CU_0192cu2</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0192cu2/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Annonaceae/" target="_blank">Annonaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Platanaceae/" target="_blank">Platanaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_008532/">FLFO_008532</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_008532/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Iteaceae/" target="_blank">Iteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0165/">CU_0165</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0165/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0760cu/">CU_0760cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0760cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010663/">FLFO_010663</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010663/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0798/">CU_0798</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0798/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_002869A/">FLFO_002869A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_002869A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Thymelaeaceae/" target="_blank">Thymelaeaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010973A/">FLFO_010973A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010973A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006689/">FLFO_006689</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006689/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0779/">CU_0779</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0779/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rutaceae/" target="_blank">Rutaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0489cu1/">CU_0489cu1</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0489cu1/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010196/">FLFO_010196</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010196/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Berberidaceae/" target="_blank">Berberidaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Betulaceae/" target="_blank">Betulaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Viburnaceae/" target="_blank">Viburnaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010429/">FLFO_010429</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010429/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010097A/">FLFO_010097A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010097A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Malvaceae/" target="_blank">Malvaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Capparaceae/" target="_blank">Capparaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Myrtaceae/" target="_blank">Myrtaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010329B/">FLFO_010329B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010329B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lardizabalaceae/" target="_blank">Lardizabalaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_011465/">FLFO_011465</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_011465/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Proteaceae/" target="_blank">Proteaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Primulaceae/" target="_blank">Primulaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0902/">CU_0902</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0902/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Meliaceae/" target="_blank">Meliaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_010308A/">FLFO_010308A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_010308A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Sapindaceae/" target="_blank">Sapindaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Simaroubaceae/" target="_blank">Simaroubaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006939B/">FLFO_006939B</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006939B/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_006502A/">FLFO_006502A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_006502A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Anacardiaceae/" target="_blank">Anacardiaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_CU_0752cu/">CU_0752cu</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/CU_0752cu/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Salicaceae/" target="_blank">Salicaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Lauraceae/" target="_blank">Lauraceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    <tr>
        <td><a href = "https://serre-lab.github.io/prj_fossil_unknown/pages/page_FLFO_005672A/">FLFO_005672A</a></td>
        <td><img src="https://storage.googleapis.com/serrelab/fossil_lens/inference_concepts2/FLFO_005672A/image.jpg" alt="Fossil Image"></td>
        <td><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rosaceae/" target="_blank">Rosaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Ulmaceae/" target="_blank">Ulmaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fagaceae/" target="_blank">Fagaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Fabaceae/" target="_blank">Fabaceae</a><br><a href="https://fel-thomas.github.io/Leaf-Lens/classes/Rhamnaceae/" target="_blank">Rhamnaceae</a></td>
        <td><input type="checkbox" name="correct"></td>
        <td><input type="checkbox" name="incorrect"></td>
        <td><input type="checkbox" name="maybe"></td>
    </tr>
    
    </table>
</div>

<button class="fixed-button" onclick="downloadJSON()">Download Responses</button>

<script>
    function downloadJSON() {
        let rows = document.querySelectorAll("table tr");
        let data = [];

        for (let i = 1; i < rows.length; i++) {
            let cells = rows[i].querySelectorAll("td");
            if (cells.length === 6) {
                let fossilName = cells[0].innerText;
                let selected = null;
                if (cells[3].querySelector("input").checked) selected = "Correct";
                if (cells[4].querySelector("input").checked) selected = "Incorrect";
                if (cells[5].querySelector("input").checked) selected = "Maybe";

                data.push({
                    "Fossil Name": fossilName,
                    "User Selection": selected
                });
            }
        }

        let blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
        let a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "fossil_responses.json";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
</script>

</body>
</html>
