from ultralytics import YOLO

# Load the YOLOv8 model (pre-trained on COCO)
model = YOLO('yolov8n.pt') 

# Train the model
results = model.train(
    data='data.yaml',       # Path to data.yaml
    epochs=50,              # Number of training epochs
    batch=16,               # Batch size
    imgsz=640,              # Image size
    device='cpu',           # Use CPU or GPU
    workers=2               # Number of dataloader workers
)

# Save the trained model
results.save('models/yolov8-soccernet.pt')
