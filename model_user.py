from ultralytics import YOLO
import cv2
import math
from collections import defaultdict

# Helper to compute Euclidean distance
def pixel_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

model = YOLO('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/The-Model.pt')

# #Run on Photo (just identificatio )
# #results = model('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/temp2.png')  
# #results[0].show()  # Show predictions

# # Run on video (identification no tracking)
# results = model('/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/images/Fimbres-Goal.mov', save=True)  # Set save=True to save output video with detections


# Run tracking on video
results = model.track(
    source='/Users/shaansekhon/Desktop/UTD/Spring 2025/Comp Vision/Project/images/Fimbres-Goal.mov',
    save=True,                # Save output video
    show=True,                # Show live video with predictions
    conf=0.3,                 # Confidence threshold
    tracker='bytetrack.yaml' # Default tracker config
)

# Tracking/distance run [HERE]

# Store center positions per track_id
track_history = defaultdict(list)

# Go through each frame's results
for result in results:
    boxes = result.boxes
    if boxes is not None and boxes.id is not None:
        for i in range(len(boxes.id)):
            track_id = int(boxes.id[i])
            cls_id = int(boxes.cls[i])
            
            # Only log players (e.g., class 0 or 1)
            if cls_id in [0, 1]:  # 0 = player, 1 = goalkeeper
                x_center = float(boxes.xywh[i][0])
                y_center = float(boxes.xywh[i][1])
                track_history[track_id].append((x_center, y_center))


# Calculate total distance per track_id

#[SUMMARY]
# Pop open the video saved in track and then simply use the printed values 
# to see pixels covered!

print("\nTotal Distance Run (in pixels):")
for track_id, points in track_history.items():
    distance = sum(pixel_distance(points[i], points[i+1]) for i in range(len(points) - 1))
    print(f"Player {track_id}: {distance:.2f} pixels")

