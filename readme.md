# SoccerNet YOLO Tracking Project

This project uses **YOLOv8** to track soccer players, the ball, and referees in SoccerNet videos. The model is trained and validated using the SoccerNet dataset.

---

## Features
Tracks players, goalkeepers, referees, and the ball  
Converts SoccerNet annotations into YOLO format  
Handles both training and validation sets  
Automatically generates YOLO-compatible labels  

---

## Utils
Download the data used with convert_to_yolo.py.
Use convert_to_yolo.py to prepare the dataset for the YOLOv8 model.
Tester.py is available to maually check images with the correlating annotations visually.
Use sample_data.py to create a new folder with whatever % of data you prefer to use.
Labels from soccerNet were not accurate, use fixed_labels.py for improving them.
mover.py moves the data files from seperate directories into one file, which is desired for training.
train_model.py/train_model_collab.py is used for training! 



## Shortcuts I forgot 
#source .venv/bin/activate

