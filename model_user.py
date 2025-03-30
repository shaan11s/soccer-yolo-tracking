from ultralytics import YOLO

model = YOLO('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/yolo_last_40epochs.pt')  # or your actual path
results = model('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/tester_img.png')  # Replace with your image path
results[0].show()  # Show predictions