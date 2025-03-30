import os
import torch
import shutil
from ultralytics import YOLO

# === CONFIGURATION ===
data_path = '/content/soccer-yolo-tracking/data_collab.yaml'
initial_model = 'yolov8n.pt'
batch = 128  # Increase for A100 GPU
imgsz = 640
device = 'cuda' if torch.cuda.is_available() else 'cpu'
max_epochs = 40
train_name = 'train_full_40_cleaned'

# === OUTPUT DIRECTORY ===
train_output_dir = os.path.join('runs/detect', train_name)
weights_path = os.path.join(train_output_dir, 'weights', 'last.pt')

# === START TRAINING ===
print(f"🚀 Starting full training from: {initial_model}")
model = YOLO(initial_model)

model.train(
    data=data_path,
    epochs=max_epochs,
    batch=batch,
    imgsz=imgsz,
    device=device,
    workers=4,
    max_det=40,
    conf=0.3,
    save=True,
    name=train_name
)

# === SAVE FINAL MODEL TO DRIVE (optional) ===
# drive_path = '/content/drive/MyDrive/yolo-checkpoints/yolo_last_40.pt'
# os.makedirs(os.path.dirname(drive_path), exist_ok=True)
# if os.path.exists(weights_path):
#     shutil.copy(weights_path, drive_path)
#     print(f"✅ Saved model to Drive: {drive_path}")
