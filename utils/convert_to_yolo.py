import os
import pandas as pd

# Define class mapping based on tracklet IDs
CLASS_MAP = {
    'player': 0,
    'goalkeeper': 1,
    'ball': 2,
    'referee': 3
}

# Paths
DATA_PATH = './data/tracking-2023/test' 
#DATA_PATH = './data/tracking-2023/train' 

def load_track_id_map(gameinfo_path):

    # [SUMMARY]
        # This function parses the gameinfo.ini file and builds a dictionary
        # that maps tracklet IDs to YOLO class IDs.
        # It's a pre-processing step used to interpret what type of object
        # each track ID refers to (player, ball, referee, etc.)

    track_id_map = {}
    with open(gameinfo_path, 'r') as f:
        for line in f:
            if line.startswith("trackletID"):
                parts = line.strip().split("=")[1].split(";")
                try:
                    track_id = int(parts[1])
                    if 'player' in parts[0]:
                        track_id_map[track_id] = CLASS_MAP['player']
                    elif 'goalkeeper' in parts[0]:
                        track_id_map[track_id] = CLASS_MAP['goalkeeper']
                    elif 'ball' in parts[0]:
                        track_id_map[track_id] = CLASS_MAP['ball']
                    elif 'referee' in parts[0]:
                        track_id_map[track_id] = CLASS_MAP['referee']
                except ValueError:
                    print(f"Skipping invalid track ID: {parts[1]}")
    return track_id_map

def convert_gt_to_yolo(gt_file, output_path, track_id_map, img_width=1920, img_height=1080):

    # [SUMMARY]
        # This function reads the ground truth bounding boxes from gt.txt,
        # uses the track_id_map to determine the object class,
        # and converts each box to YOLO format (class_id x_center y_center width height).
        # The results are saved as .txt label files, one per frame, in the specified output folder.

    df = pd.read_csv(gt_file, header=None)

    for _, row in df.iterrows(): #underscore '_' is for ignoring row number
        frame_id, track_id, x, y, w, h, confidence = row[:7]
        class_id = track_id_map.get(int(track_id), -1)
        #in the GT file we have extra rows of -1 which are essentially just ignored, dont worry about them.
        if class_id == -1:
            continue
        
        # Convert to YOLO format (normalized 0-1)
        x_center = (x + w / 2) / img_width
        y_center = (y + h / 2) / img_height
        w = w / img_width
        h = h / img_height
        
        # Create labels folder if it doesn't exist inside the sequence folder
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # YOLO label file should match frame number (e.g., 000001.txt)
        label_file = os.path.join(output_path, f"{int(frame_id):06d}.txt")
        with open(label_file, 'a') as f:
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

        print(f"Writing to {label_file} with class {class_id}")

def process_all_sequences():

    # [SUMMARY]
        # This function loops through each sequence folder (like "SNMOT-060") inside the dataset directory.
        # For each sequence, it builds the full path to important files: 
        # - "gameinfo.ini" (for class mapping)
        # - "gt/gt.txt" (for bounding box annotations)
        # If both files exist, it builds a mapping from track IDs to class IDs (player, ball, etc.)
        # and converts the ground truth boxes in gt.txt to YOLO format. (We use this box to compute loss function)
        # The converted label files are saved inside a "labels/" folder within each sequence.


    for seq in os.listdir(DATA_PATH):
        seq_path = os.path.join(DATA_PATH, seq)
        if not os.path.isdir(seq_path):
            continue

        print(f"Processing sequence: {seq}")

        gameinfo_path = os.path.join(seq_path, 'gameinfo.ini')
        gt_path = os.path.join(seq_path, 'gt/gt.txt')

        if os.path.exists(gameinfo_path) and os.path.exists(gt_path):
            track_id_map = load_track_id_map(gameinfo_path)
            
            # Write labels INSIDE each sequence folder
            labels_output_path = os.path.join(seq_path, 'labels')
            convert_gt_to_yolo(gt_path, labels_output_path, track_id_map)

if __name__ == "__main__":
    process_all_sequences()
    print("✅ All sequences converted to YOLO format!")
