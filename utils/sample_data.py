import os
import random
import shutil

def sample_snmot_split(base_path, split='train', sample_ratio=0.1):
    input_base = os.path.join(base_path, split)
    output_base = os.path.join(base_path, 'sampled', split)

    for snmot_folder in os.listdir(input_base):
        folder_path = os.path.join(input_base, snmot_folder)
        if not os.path.isdir(folder_path):
            continue

        print(f"📁 Sampling from {split}/{snmot_folder}...")

        # Images and labels are both in this folder:
        all_labels_path = os.path.join(folder_path, 'all_labels')
        output_labels_path = os.path.join(output_base, snmot_folder, 'all_labels')
        os.makedirs(output_labels_path, exist_ok=True)

        # Get all image files
        image_files = [f for f in os.listdir(all_labels_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not image_files:
            print(f"⚠️ No images found in {all_labels_path}")
            continue

        sample_size = max(1, int(len(image_files) * sample_ratio))
        sampled_images = random.sample(image_files, sample_size)

        for img_file in sampled_images:
            # Copy image
            src_img_path = os.path.join(all_labels_path, img_file)
            dst_img_path = os.path.join(output_labels_path, img_file)
            shutil.copy(src_img_path, dst_img_path)

            # Copy corresponding label
            base_name = os.path.splitext(img_file)[0]
            label_file = base_name + '.txt'
            src_label_path = os.path.join(all_labels_path, label_file)
            dst_label_path = os.path.join(output_labels_path, label_file)

            if os.path.exists(src_label_path):
                shutil.copy(src_label_path, dst_label_path)

        print(f"✔️ Sampled {sample_size} images from {snmot_folder} ({split})")

def sample_train_and_test(base_path, sample_ratio=0.1):
    for split in ['train', 'test']:
        sample_snmot_split(base_path, split=split, sample_ratio=sample_ratio)

# ✅ Run the script
if __name__ == "__main__":
    sample_train_and_test(base_path='data/tracking-2023', sample_ratio=0.1)
