import os
import torch
import gc
import shutil
from ultralytics import YOLO

# [SUMMARY]
# This was essentially borrowed from the ultralytics YOLO 8 Github repo (read me file)
# Adjust as needed!

# === CONFIGURATION ===
data_path = 'data.yaml'
initial_model = 'yolov8n.pt'
batch = 2
imgsz = 320
device = 'mps'
max_epochs = 40
chunk_size = 5
train_base_dir = 'runs/detect'

# === PATHS ===
weights_base = os.path.join(train_base_dir, 'train/weights')
weights_path = os.path.join(weights_base, 'last.pt')

# === DETERMINE STARTING POINT ===
if os.path.exists(weights_path):
    model = YOLO(weights_path)
    print(f" Resuming from checkpoint: {weights_path}")
    current_epoch = int(weights_path.split("_")[-1].split(".")[0]) if "epoch" in weights_path else 0
else:
    model = YOLO(initial_model)
    print(f" Starting fresh from base model: {initial_model}")
    current_epoch = 0

chunk_num = 1

# === CHUNKED TRAINING LOOP ===
while current_epoch < max_epochs:
    target_epoch = min(current_epoch + chunk_size, max_epochs)
    chunk_name = f"train_chunk_{chunk_num}"
    chunk_output_dir = os.path.join(train_base_dir, chunk_name)

    print(f"\n Training chunk {chunk_num}: epoch {current_epoch + 1} → {target_epoch}")

    model.train(
        data=data_path,
        epochs=target_epoch,
        batch=batch,
        imgsz=imgsz,
        device=device,
        workers=1,
        max_det=40,
        conf=0.3,
        resume=True if current_epoch > 0 else False,
        save=True,
        name=chunk_name  # Saves logs to: runs/detect/train_chunk_#
    )

    # === BACKUP CHECKPOINT ===
    backup_path = os.path.join(weights_base, f"last_epoch_{target_epoch}.pt")
    if os.path.exists(weights_path):
        shutil.copy(weights_path, backup_path)
        print(f" Backed up weights to {backup_path}")

    # === CLEAN UP MPS MEMORY ===
    del model
    gc.collect()
    torch.mps.empty_cache()
    print("🧹 Cleared GPU memory")

    # === RELOAD MODEL FOR NEXT CHUNK ===
    model = YOLO(weights_path)
    current_epoch = target_epoch
    chunk_num += 1
