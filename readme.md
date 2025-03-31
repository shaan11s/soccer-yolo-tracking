# SoccerNet YOLOv8 Tracking Project

This project uses **YOLOv8** to detect and track soccer players, referees, and the ball in match footage from the **SoccerNet** dataset. The goal is to enable free and accurate soccer analytics through computer vision.

![Working Example](images/working-example-1.png)

---

## Features

- Detects **players**, **goalkeepers**, **referees**, and the **ball**
- Converts SoccerNet annotations into YOLO-compatible format
- Supports both **training** and **validation** data pipelines
- Includes label verification and correction scripts
- Clean modular codebase for preprocessing, training, and testing

---

## Training Results Summary

The YOLOv8 model was trained for 40 epochs on the SoccerNet dataset to detect players, goalkeepers, referees, and the ball, and then again for another 40 epochs on the Kaggle soccer detection dataset. 

Loss curves show steady improvement across box, classification, and distance losses.

Validation loss closely tracks training loss, indicating good generalization.

Recall steadily improves to ~0.73.

mAP50 hits ~0.83, and mAP50-95 reaches ~0.58.

---

## Structure

Project/
│
├── data/                   # Original and converted SoccerNet data
├── fix-this-data/          # Label cleanup
├── runs/                   # YOLOv8 training output
├── utils/                  # Helper scripts
├── images/                 # Example input/output
├── train_model.py          # Training script
├── data.yaml               # YOLO class config
└── README.md               # You’re here!

---

## Utilities

| Script | Purpose |
|--------|---------|
| `convert_to_yolo.py` | Converts SoccerNet annotations into YOLOv8 format |
| `tester.py` | Visually checks labels and annotations for each frame |
| `sample_data.py` | Extracts a % sample of the dataset for lightweight experiments |
| `fixed_labels.py` | Cleans mislabeled annotations from original dataset |
| `mover.py` | Merges scattered files into a single YOLO-style structure |
| `train_model.py` / `train_model_collab.py` | Main training scripts (local or Google Colab) |

---

## Images Folder

- Includes test images and YOLOv8 predictions for reference  
- Use these to validate your model or showcase its performance

---

## Developer Notes

Some quick commands I kept forgetting:

```bash
# Activate virtual environment
source .venv/bin/activate

