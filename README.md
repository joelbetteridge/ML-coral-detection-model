# Staghorn Coral AI Detection Model

**Automated semantic segmentation for staghorn coral restoration monitoring**

---

## Overview

This repository contains the first automated coral detection models deployed at [Reef Renewal Foundation Bonaire (RRFB)](https://reefrenewalbonaire.org). The model uses DeepLabV3+ trained in TagLab to achieve fast and consistent annotation of Staghorn in local underwater orthomosaics for restoration monitoring. It uses existing TagLab scripts, custom core source patches, and preprocessing utilities (see SOP.pdf) Six iterations were created, two of which are highlighted here:
- **Stag_v1++** (Baseline Production): Optimized with Focal Tversky loss at batch size 8 which provided an initial 98% balanced F1 baseline.
- **Stag_v1FB** (Boundary Refined): Enhanced with a hybrid **Focal + Boundary Loss** schedule to increase edge precision.

Staghorn corals (*Acropora cervicornis*) are a critically endangered species in Caribbean reef ecosystems. Scalable monitoring of restoration sites over time intervals is essential for success, and manual annotation of large orthomosaics (500 + megapixels) is not only time-consuming (20+ hours) but also subjective. This model aims to reduce annotation bottlenecks for RRFB while maintaining high accuracy.

---

## What This Model Does


The model performs **pixel-wise semantic segmentation** on underwater orthomosaics, automatically identifying and delineating staghorn coral colonies. It outputs a binary segmentation mask (staghorn vs. background) that can be:

- Reviewed and refined by human annotators
- Used to track coral coverage over time
- Integrated into RRFB's restoration monitoring pipeline

---

### Training Details & Ablation Setup

| Hyperparameter / Setting | `Stag_v1++` | `Stag_v1FB` |
| :--- | :--- | :--- |
| **Loss Function** | Focal Tversky ($\alpha=0.6, \gamma=0.75$) | Focal + Boundary Loss (Epochswitch = 10, Epochtrans = 10) |
| **Learning Rate** | $0.00005$ | $0.000025$ (Halved to suppress gradient spikes) |
| **Batch Size** | 8 | 4 (Stabilized with step damping) |
| **Completed Epochs** | 13 (Interrupted baseline) | 50 (Full boundary convergence) |

### Similarities

- **Total pixels** ~700 million
- **Class balance** 95% background, 5% staghorn
- **Training images:** 513×513 RGB tiles (extracted from full orthomosaics)
- **Pixel Normalization** [0.5932, 0.5870, 0.5226]
- **Backbone** ResNet50 (output stride 16)
- **Scale Factor** 0.9

---


## Results & Methodology Note

<<<<<<< HEAD
## Currently doing stats on Stag_v1FB , below is the results from Stag_v1++

Model evaluated on unseen test orthomosaic Site = (Pink Beac,  Timescale=  2,Size =  ~743 megapixels).
=======
Model evaluated on unseen test orthomosaic Site = (Pink Beach,  Timescale=  2,Size =  ~743 megapixels).
>>>>>>> 9534e85791741b0c9b42bc6b94c12a6792ce7100

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

- **AI segmentation:** ~30 minutes per full orthomosaic
- **Human review & refinement:** ~150 minutes additional
- **Total workflow:** ~3 hours per site (vs. 20+ hours for manual annotation from scratch)

### Coverage

Model detected staghorn coverage at approximately **5.6%** of test orthomosaic, consistent with human annotations (5.62%).

---

## Usage

### Deployment in TagLab

1. Model weights are registered in `config.json` as `Stag_v1++.net`
2. Open any orthomosaic in TagLab
3. Click **"Fully automatic semantic segmentation"**
4. Select the Staghorn classifier
5. Preview output and refine annotations as needed

### Files in This Repository

- **`SOP.md`** — Complete standard operating procedure (18 steps) for training and deploying models
- **`scripts/`** — Utility scripts for data preprocessing
  - `compute_dataset_avg.py` — Calculates per-channel pixel normalization
  - `fix_channel_mismatch.py` — Converts RGBA images to RGB (handles transparency)
  - `dataset_merger` — Powershell script to edit exisitng pipeline to TagLab needs
- **`models/`**
  - `config.json` — Model configuration and hyperparameters
  - `Stag_v1++-val-metrics` — Confusion matrix of Stag_v1++
- **`figures/`** — Sample segmentation outputs before/after annotation refinement

---

## Technical Notes

### Critical Backend Patches (TagLab Source Modifications)

Training DeepLabV3+ with custom boundary loss under modern Python environments required several programmatic interventions:

- **NumPy Boolean Deprecation (`models/losses.py`):** Replaced legacy `np.bool` with Python `bool` across distance-transform conversion arrays (`one_hot2dist`) to prevent runtime failure in modern environments.
- **Device Tensor Mismatches (`models/losses.py`):** Corrected boundary loss normalization bounds (`xmin`, `xmax`) from `torch.tensor` declarations to primitive floats (`-90.0`, `90.0`) to avoid fatal CPU/GPU tensor mismatch exceptions during epoch 10 turnover.
- **Validation Memory Overflow (`models/training.py`):** Disabled memory-heavy full-dataset flattening (`flag_compute_mIoU = False`) during test passes to prevent RAM exhaustion on large test suites. Changed dtype = int to int.64 for windows system application.
- **Alpha Channel Harmonization (`scripts/fix_channel_mismatch.py`):** Developed a standalone pipeline to detect and flatten 4-channel RGBA tiles onto black backgrounds, eliminating dimension broadcast crashes in `computeAverage()`.

### Known Limitations

1.  **3D Challenges:** In cases where fish are above live staghorn, the model learns fish = staghorn
2. **Growth tips:** Most post AI processing is used to expand staghorn very marginally as the growth tips are not being defined, more training will likely fix this.
3. **Edge effects:** Segmentation is less reliable at orthomosaic tile boundaries; overlap-based inference can mitigate this.
4. **Lighting variation:** Model generalizes well across Bonaire dive sites but may require retraining if working in significantly different light conditions or locations.

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

## AI integrity 

These scripts were AI assisted and human edited.