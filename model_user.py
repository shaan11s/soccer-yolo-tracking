from ultralytics import YOLO

model = YOLO('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/The-Model.pt')  # or your actual path
results = model('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/temp2.png')  # Replace with your image path
results[0].show()  # Show predictions