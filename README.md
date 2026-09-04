# Staghorn Coral AI Detection Model

**Automated semantic segmentation for staghorn coral restoration monitoring**

---

## Overview

This repository contains the first automated coral detection model deployed at [Reef Renewal Foundation Bonaire (RRFB)](https://reefrenewalbonaire.org). The model uses DeepLabV3+ semantic segmentation CNN trained in TagLab to achieve fast and consistent annotation of Staghorn in local underwater orthomosaics for restoration monitoring.

Staghorn corals (*Acropora cervicornis*) are a critically endangered species in Caribbean reef ecosystems.Scalable monitoring of restoration sites over time intervals is essential for success, and manual annotation of large orthomosaics (500 + megapixels) is not only time-consuming (20+ hours) but also subjective. This model aims to reduce annotation bottlenecks for RRFB while maintaining high accuracy.

---

## What This Model Does


The model performs **pixel-wise semantic segmentation** on underwater orthomosaics, automatically identifying and delineating staghorn coral colonies. It outputs a binary segmentation mask (staghorn vs. background) that can be:

- Reviewed and refined by human annotators
- Used to track coral coverage over time
- Integrated into RRFB's restoration monitoring pipeline

---

## Model Architecture & Training

- **Architecture:** DeepLabV3+ (encoder-decoder with atrous convolution)
- **Backbone:** ResNet50
- **Training Framework:** TagLab (semantic segmentation toolbox)
- **Datasets:** Trained on 6 orthomosaics split into 3-6 working areas
- **Validation:** 70% training / 15% validation / 15% test split

### Training Details

- **Total annotations:** Thousands of staghorn instances across multiple orthomosaics
- **Training images:** 513×513 RGB tiles (extracted from full orthomosaics)
- **Epochs:** Trained until convergence (~20 epochs)
- **Scale factor:** 0.9
- **Pixel normalization:** [0.5932, 0.5870, 0.5226] (per-channel means)

---


## Results & Methodology Note

Model evaluated on unseen test orthomosaic Site = (Pink Beac,  Timescale=  2,Size =  ~743 megapixels).

**Manual refinement:** Following initial AI segmentation, I performed targeted human editing (~3 hours) to remove false positives (primarily fish and soft coral misclassifications) and refine staghorn borders for monitoring consistency. Large staghorn clusters were accepted as-is where the AI output met acceptable annotation standards, as determining live vs. dead coral tissue is subjective and outside the scope of this validation.

**Important caveat:** These results represent AI performance after *minimal* post-processing, not a rigorous blind comparison. Some AI annotations were accepted due to practical monitoring standards rather than perfect accuracy, which may slightly inflate reported metrics. The model is fit for purpose in RRFB's workflow (rapid, consistent baseline for human review) rather than claim publication-ready perfection.

---


### Overall Performance

| Metric | Value |
|--------|-------|
| **Accuracy** | 99.79% |
| **Precision** | 98.28% |
| **Recall** | 97.94% |
| **F1 Score** | 98.11% |

### Pixel-Level Breakdown

| Classification | Pixels | Percentage |
|---|---|---|
| True Positives (correct staghorn) | 40,966,966 | 5.51% |
| True Negatives (correct background) | 701,526,877 | 94.28% |
| False Positives (AI only) | 862,660 | 0.12% |
| False Negatives (Human only) | 716,533 | 0.10% |
| **Total Disagreement** | 1,579,193 | **0.21%** |

### Error Analysis

Out of 767 total annotations, model errors were distributed as:

| Error Type | Count |
|---|---|
| Fish (misclassified as staghorn) | 63 |
| Soft coral | 9 |
| Sand/dead coral | 2 |
| Boulder | 2 |
| Fire coral | 1 |

**Key finding:** Most errors are false positives from morphologically similar organisms (fish, soft corals). Fine-tuning the training dataset or post-processing could reduce these further Fish appearing above live staghorn poses a great challenge in training..

---

## Practical Performance

### Speed

- **AI segmentation:** ~40 minutes per full orthomosaic
- **Human review & refinement:** ~120 minutes additional
- **Total workflow:** ~3 hours per site (vs. 20+ hours for manual annotation from scratch)

### Coverage

Model detected staghorn coverage at approximately **5.6%** of test orthomosaic, consistent with human annotations (5.62%).

---

## Usage

### Deployment in TagLab

1. Model weights are registered in `config.json` as `Stag_v1.net`
2. Open any orthomosaic in TagLab
3. Click **"Fully automatic semantic segmentation"**
4. Select the Staghorn classifier
5. Preview output and refine annotations as needed

### Files in This Repository

- **`SOP.md`** — Complete standard operating procedure (18 steps) for training and deploying models
- **`scripts/`** — Utility scripts for data preprocessing
  - `compute_dataset_avg.py` — Calculates per-channel pixel normalization
  - `fix_channel_mismatch.py` — Converts RGBA images to RGB (handles transparency)
  - `image_merger` — Powershell script to edit exisitng pipeline to TagLab needs
- **`models/config.json`** — Model configuration and hyperparameters
- **`figures/`** — Sample segmentation outputs before/after annotation refinement

---

## Technical Notes

### Known Limitations

1  **3D Challenges:** In cases where fish are above live staghorn, the model learns fish = staghorn; extensive training would be needed to combat this
2. **Growth tips:** Most post AI processing is used to expand staghorn very marginally as the growth tips are not being defined, more training will likely fix this.
3. **Edge effects:** Segmentation is less reliable at orthomosaic tile boundaries; overlap-based inference can mitigate this.
4. **Lighting variation:** Model generalizes well across Bonaire dive sites but may require retraining if working in significantly different light conditionsor locations..

### Improvements for Next Version (Stag_v2)

- Expand training dataset with >3 new sites to improve robustness and fix growth tips limitation
- Add negative examples (fish,soft corals, fire corals) to reduce false positives
- Implement multi-class segmentation to simultaneously detect other coral species`

---

## Impact

This model directly supports RRFB's coral restoration workflow:

- **Reduces annotation time** by ~85% per site
- **Eliminates subjectivity** in coral identification
- **Enables rapid re-monitoring** to track colony growth over restoration timelines
- **Scales to new sites** with minimal retraining once deployed

---

## References

- TagLab: Semantic segmentation for reef monitoring — https://github.com/torchillasm/TagLab
- DeepLabV3+: Chen et al., *Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation* (ECCV 2018)
- RRFB Restoration Program — https://reefrenewalbonaire.org

---

## Author

**Joel Betteridge**  
Coral Reef Restoration Technician Intern
Reef Renewal Foundation Bonaire  
University of York, BSc Ecology (Third Year)

---

## License

This model and SOP are provided as-is for reef restoration research. Please contact RRFB before using this model for commercial purposes.