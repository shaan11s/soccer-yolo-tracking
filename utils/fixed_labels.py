import os
import shutil
from glob import glob

# Image dimensions
IMG_WIDTH = 1920
IMG_HEIGHT = 1080

# Class IDs
PLAYER_ID = 0
BALL_ID = 2

# Threshold: ball must be smaller than this fraction of average player area
BALL_AREA_RATIO = 0.25  # Ball must be smaller than 25% of average player size

# Source and destination root
SRC_ROOT = 'data/tracking-2023'
DEST_ROOT = 'fixed_data'

# Folders to check: train and test
splits = ['train', 'test']

all_label_paths = []
for split in splits:
    pattern = os.path.join(SRC_ROOT, split, 'SNMOT-*', 'all_labels', '*.txt')
    all_label_paths.extend(glob(pattern))

print(f"🔍 Found {len(all_label_paths)} label files to process.")

for label_path in all_label_paths:
    with open(label_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    labels = []
    for line in lines:
        parts = line.split()
        if len(parts) != 5:
            continue  # skip malformed lines
        cls_id, xc, yc, w, h = int(parts[0]), float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])
        abs_w = w * IMG_WIDTH
        abs_h = h * IMG_HEIGHT
        area = abs_w * abs_h
        labels.append({'cls': cls_id, 'xc': xc, 'yc': yc, 'w': w, 'h': h, 'area': area})

    if len(labels) > 1:
        smallest = min(labels, key=lambda l: l['area'])
        smallest_is_player = smallest['cls'] == PLAYER_ID
        has_ball = any(l['cls'] == BALL_ID for l in labels)

        if smallest_is_player and has_ball:
            # Swap smallest (player → ball) and one ball (ball → player)
            smallest['cls'] = BALL_ID
            for l in labels:
                if l['cls'] == BALL_ID:
                    l['cls'] = PLAYER_ID
                    break

        # Optional: remove balls that are too big compared to players
        player_areas = [l['area'] for l in labels if l['cls'] == PLAYER_ID]
        if player_areas:
            avg_player_area = sum(player_areas) / len(player_areas)
            labels = [l for l in labels if not (l['cls'] == BALL_ID and l['area'] > avg_player_area * BALL_AREA_RATIO)]

    # === WRITE FIXED FILE ===
    rel_path = os.path.relpath(label_path, SRC_ROOT)
    parts = rel_path.split(os.sep)
    parts[-2] = 'fixed_labels'
    dest_label_path = os.path.join(DEST_ROOT, *parts)
    os.makedirs(os.path.dirname(dest_label_path), exist_ok=True)

    with open(dest_label_path, 'w') as f:
        for l in labels:
            f.write(f"{l['cls']} {l['xc']} {l['yc']} {l['w']} {l['h']}\n")

    # === COPY CORRESPONDING IMAGE INTO fixed_labels/ ===
    filename = os.path.splitext(os.path.basename(label_path))[0] + '.jpg'
    img_path = os.path.join(os.path.dirname(label_path), filename)
    if os.path.exists(img_path):
        dest_img_path = os.path.join(os.path.dirname(dest_label_path), filename)
        shutil.copy(img_path, dest_img_path)
        print(f"✅ Fixed + copied: {dest_img_path}")
    else:
        print(f"⚠️ Image not found for: {img_path}")

print("🎉 Label auto-fix complete. Files saved under 'fixed_data/'")