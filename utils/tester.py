import cv2
import os

# [SUMMARY]
    # check to see if the labels and boxes are actually 
    # working after conversaion 

# Set paths to test 
img_path = "/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/Football-Player-Detection.v8-resized1280_tile2x2_aug3x.yolov8/train/images/0_pp_jpg.rf.7d9197db792cf28671b6cbe24110044c.jpg"
label_path = "/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/Football-Player-Detection.v8-resized1280_tile2x2_aug3x.yolov8/train/labels/0_pp_jpg.rf.7d9197db792cf28671b6cbe24110044c.txt"

# Image size
img_width = 1280
img_height = 1280

# Load image
image = cv2.imread(img_path)

# Class names (just for visualization)
class_names = {0: 'Player', 1: 'Goalkeeper', 2: 'Ball', 3: 'Referee'}

# Read label file
with open(label_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()
    class_id = int(parts[0])
    x_center = float(parts[1]) * img_width
    y_center = float(parts[2]) * img_height
    w = float(parts[3]) * img_width
    h = float(parts[4]) * img_height

    # Convert to top-left corner
    x1 = int(x_center - w / 2)
    y1 = int(y_center - h / 2)
    x2 = int(x_center + w / 2)
    y2 = int(y_center + h / 2)

    # Draw box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    label = class_names.get(class_id, str(class_id))
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

# Show image
cv2.imshow("Labeled Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
