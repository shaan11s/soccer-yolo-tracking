import os
import shutil

# Define the source path (path to train folder)
data_path = './data/tracking-2023/test' #
data_path = './data/tracking-2023/train' 

# Go into each SNMOT-* folder
for seq in os.listdir(data_path):
    seq_path = os.path.join(data_path, seq)
    img_path = os.path.join(seq_path, 'img1')
    label_path = os.path.join(seq_path, 'labels')
    all_labels_path = os.path.join(seq_path, 'all_labels')

    if os.path.exists(img_path) and os.path.exists(label_path):
        # Create all_labels folder if it doesn't exist
        os.makedirs(all_labels_path, exist_ok=True)
        
        # Get list of image and label files (without extensions)
        img_files = {os.path.splitext(f)[0] for f in os.listdir(img_path) if f.endswith('.jpg')}
        label_files = {os.path.splitext(f)[0] for f in os.listdir(label_path) if f.endswith('.txt')}

        # Find matching pairs
        matched_files = img_files.intersection(label_files)

        for file in matched_files:
            img_src = os.path.join(img_path, f"{file}.jpg")
            label_src = os.path.join(label_path, f"{file}.txt")

            img_dst = os.path.join(all_labels_path, f"{seq}_{file}.jpg")
            label_dst = os.path.join(all_labels_path, f"{seq}_{file}.txt")

            # Copy matching files to all_labels/
            shutil.copy(img_src, img_dst)
            shutil.copy(label_src, label_dst)

            print(f"Copied {file}.jpg and {file}.txt to {all_labels_path}")

print("Done organizing labels!")
