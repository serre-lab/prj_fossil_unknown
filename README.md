# Fossil Leaf Lens

> A machine learning tool to help paleobotanists identify leaf fossils

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Authors

**Ivan Felipe Rodriguez**🌿<sup>1</sup>, **Thomas Fel**🌿<sup>2</sup>, **Gaurav Gaonkar**<sup>1</sup>, **Mohit Vaishnav**<sup>1</sup>, **Herbert Meyer**<sup>4</sup>, **Peter Wilf**<sup>3</sup> & **Thomas Serre**<sup>1</sup>

🌿 *Joint First Authors*

<sup>1</sup> Brown University  
<sup>2</sup> Kempner Institute, Harvard University  
<sup>3</sup> Pennsylvania State University  
<sup>4</sup> Florissant Fossil Beds, National Park Service

---

## Overview

Fossil Leaf Lens is an innovative AI-powered web application that addresses one of paleobotany's most challenging puzzles: identifying fossil angiosperm leaves. These organs are often abundant yet notoriously difficult to classify, especially in the absence of organic attachments or cuticles, due to their complexity, variation, and the often limited quality and quantity of available images.

Through the power of AI and computer vision, we have developed a deep learning model that synthesizes photorealistic fossil images from extant cleared and x-rayed leaves, increasing the sample size of "fossil" image collections for training. This approach allows machine identifications of fossil and extant leaves at the family level—the starting point for most investigations—with levels of accuracy sufficient to provide useful suggestions for experts.

### Key Features

- **Automated Fossil Identification**: Deep learning model predicts family-level classifications for fossil leaves
- **Interactive Feedback System**: Expert paleobotanists can review and validate predictions
- **Similar Specimen Matching**: Displays visually similar specimens from the training dataset
- **Concept Visualization**: Shows interpretable visual patterns the model uses for classification
- **Comprehensive Dataset**: Focused on Florissant Fossil Beds (late Eocene, Colorado) specimens

### Demo

![Fossil Leaf Lens Navigation Guide](docs/images/fossil.gif)

*Interactive navigation guide showing how to use the Fossil Leaf Lens website*

---

## Project Structure

```
unknown_fossils/
├── docs/                          # Generated HTML/Markdown documentation
│   ├── images/                    # Static images (logo, GIFs)
│   ├── pages/                     # Individual fossil specimen pages
│   │   ├── unknown/              # Unknown fossil specimens
│   │   └── unidentified/         # Unidentified fossil specimens
│   ├── index.md                  # Homepage
│   └── unidentified_table.md     # Feedback table page
├── generate_home.py               # Generate homepage HTML
├── generate_pages.py              # Generate individual fossil pages
├── generate_unidentified_table.py # Generate feedback table
├── mkdocs.yml                     # MkDocs configuration
└── README.md                      # This file
```

---

## Website Features

### 1. Predicted Fossil Identification

Explore predicted fossil identifications through detailed webpages for each specimen. Each page includes:

- **Fossil Information Card**: Dataset catalog number, primary catalog number, and model predictions
- **Similar Specimens**: Images from the training dataset most similar to the specimen
- **Concepts**: Visual patterns the model uses for classification, corresponding to diagnostic leaf architecture traits

#### Metadata Resources

- [Florissant CU Metadata](https://docs.google.com/spreadsheets/d/1IxU4YjUBWdJyolYbKlNUQetb7sDlN3sV/edit?usp=sharing&ouid=117124297544856301307&rtpof=true&sd=true)
- [Florissant FLFO Metadata](https://docs.google.com/spreadsheets/d/1FIeJoNFIOy22oGVMDgrBZ94EWQ9OZqGLprjPYZRJuLY/edit?usp=sharing)

### 2. Feedback Table

The feedback table allows expert paleobotanists to evaluate model predictions:

- View unidentified fossil specimens with images
- Review top 5 model predictions for each specimen
- Provide feedback using color-coded options:
  - 🟢 **Plausible**: One or more families are likely correct
  - 🔴 **Impossible**: No predictions make sense
  - 🟡 **Not Sure**: Further study needed
  - ⚪ **Not Applicable**: Specimen doesn't belong

---

## Dataset

The project focuses on leaf fossils from the **Florissant Fossil Beds** (late Eocene, Colorado), one of the world's most well-studied and photo-documented fossil sites. The images were gathered over many years by Dr. Herbert Meyer (retired, National Parks Service) and assistants from museums around the world.

### References

- Meyer et al. (2008). GSA Special Papers 435. [DOI: 10.1130/2008.2435(11)](https://doi.org/10.1130/2008.2435(11))
- Wilf et al. (2021). PhytoKeys. [DOI: 10.3897/phytokeys.187.72350](https://doi.org/10.3897/phytokeys.187.72350)
- Image Collection: [DOI: 10.25452/figshare.plus.14980698.v2](https://doi.org/10.25452/figshare.plus.14980698.v2)

---

## Technical Details

### Model Training

The deep learning model:
- Synthesizes photorealistic fossil images from extant cleared and x-rayed leaves
- Trained on vetted Florissant fossils and cleared/x-rayed leaf images
- Predicts family-level classifications for fossil angiosperm leaves
- Uses interpretable "concepts" corresponding to diagnostic leaf architecture traits

### Concepts

Concepts are visual or structural patterns in specimens that the model uses for classification. These often correspond to traditional taxonomic features such as:
- Leaf margins
- Venation patterns
- Symmetry
- Other diagnostic leaf architecture traits

For more information, see Spagnuolo et al. (2022), International Journal of Plant Sciences. [DOI: 10.1002/ajb2.1842](https://doi.org/10.1002/ajb2.1842)

---

## Usage

### For Paleobotanists

1. Navigate to the [Fossil Leaf Lens website](https://serre-lab.github.io/prj_fossil_unknown/)
2. Browse predicted fossil identifications from the navigation menu
3. Review individual specimen pages with detailed predictions
4. Use the Feedback Table to evaluate and provide feedback on predictions
5. Download your feedback as a JSON file and send to: [ivan_felipe_rodriguez@brown.edu](mailto:ivan_felipe_rodriguez@brown.edu)

### For Developers

1. Clone the repository
2. Install dependencies (if required)
3. Run generation scripts:
   ```bash
   python generate_home.py
   python generate_pages.py
   python generate_unidentified_table.py
   ```
4. Build with MkDocs (if using MkDocs):
   ```bash
   mkdocs build
   ```

---

## Limitations & Disclaimers

- The dataset includes many fossil samples that are badly preserved and may lack detail needed for accurate classification
- Some images may include monocots, non-angiosperms, reproductive organs, or non-plant fossils that are undersampled in the training dataset
- The model can only predict families present in its training dataset ([list available here](https://docs.google.com/document/d/178X6Stw9_J4k-Ib9lp8eWAH8tUv86rtg8VBqZPeVuWw/edit?usp=sharing))
- We recommend skipping poorly preserved or inapplicable specimens

---

## Contact

For questions, feedback, or collaboration inquiries, please contact:

**Ivan Felipe Rodriguez**  
📧 [ivan_felipe_rodriguez@brown.edu](mailto:ivan_felipe_rodriguez@brown.edu)  
🏛️ Brown University

---

## Citation

If you use Fossil Leaf Lens in your research, please cite:

```bibtex
@article{fossil_leaf_lens_2024,
  title={Fossil Leaf Lens: A Machine Learning Tool for Paleobotanical Leaf Identification},
  author={Rodriguez, Ivan Felipe and Fel, Thomas and Gaonkar, Gaurav and Vaishnav, Mohit and Meyer, Herbert and Wilf, Peter and Serre, Thomas},
  journal={Manuscript in preparation},
  year={2024}
}
```

---

## Acknowledgments

We thank Dr. Herbert Meyer for his extensive work gathering and cataloging the Florissant Fossil Beds specimens, and all museums and institutions that contributed images to this dataset.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**We invite you to explore this innovative blend of paleobotany and artificial intelligence, and to join us in refining the art and science of fossil leaf identification!** 🌿🔬

