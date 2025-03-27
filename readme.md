# SoccerNet YOLO Tracking Project

This project uses **YOLOv8** to track soccer players, the ball, and referees in SoccerNet videos. The model is trained and validated using the SoccerNet dataset.

---

## Features
Tracks players, goalkeepers, referees, and the ball  
Converts SoccerNet annotations into YOLO format  
Handles both training and validation sets  
Automatically generates YOLO-compatible labels  

---

## Dataset Structure
The dataset is organized as follows:

```plaintext
data/
├── tracking/
│   ├── tracking-2023/
│       ├── train/
│           ├── SNMOT-060/
│               ├── img1/       # Training images
│               ├── gt/         # Ground truth files
│               ├── labels/     # YOLO format labels
│               ├── gameinfo.ini
│               ├── seqinfo.ini
│       ├── test/
│           ├── SNMOT-116/
│               ├── img1/       # Test images
│               ├── gt/         # Ground truth files
│               ├── labels/     # YOLO format labels
│               ├── gameinfo.ini
│               ├── seqinfo.ini





shortcuts for me 
#source .venv/bin/activate