import os
import shutil
from datetime import datetime

# USE THIS
# USE AMBIENT LABELS FROM ROBOFLOW AND APPLY LABELS TO ALL OTHER DATASETS' IMAGES

# Paths
# plain RGB images folder from Google Drive
source_folder = '/Users/ray/Downloads/NIR'

# new folder created by yourself
destination_folder = '/Users/ray/Desktop/combinedLED_day_NIRonly'

# roboflow's folder, pre labelled ambient RGB in train, test and valid folders
label_folder = '/Users/ray/Downloads/project-101-disease-detection.v36-21-9-24-daytime-65images.yolov8'

# Create folder structure for the output
for split in ['valid', 'train', 'test']:
    os.makedirs(os.path.join(destination_folder, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(destination_folder, split, 'labels'), exist_ok=True)

# Function to match files based on the same timestamp and copy them
def copy_files_with_matching_time(split):
    label_split_folder = os.path.join(label_folder, split, 'labels')
    source_files = os.listdir(source_folder)

    # Iterate over each label file in the split folder
    for label_file in os.listdir(label_split_folder):
        if label_file.endswith('.txt'):
            # Extract the timestamp from the label filename
            try:
                label_time_str = '_'.join(label_file.split('_')[1:4])
                label_time = datetime.strptime(label_time_str, '%Y%m%dT%H_%M_%S')
            except ValueError:
                print(f"Skipping label file {label_file} due to unrecognized date format")
                continue

            # Find the matching image with the exact same timestamp
            matching_image = None
            for source_file in source_files:
                if source_file.endswith('.png'):
                    try:
                        source_time_str = '_'.join(source_file.split('_')[1:4])
                        source_time = datetime.strptime(source_time_str, '%Y%m%dT%H_%M_%S')
                    except ValueError:
                        print(f"Skipping source file {source_file} due to unrecognized date format")
                        continue

                    # Check if the timestamp matches exactly
                    if label_time == source_time:
                        matching_image = source_file
                        break

            # If a matching image is found, copy both the image and the label
            if matching_image:
                # Copy image
                image_path = os.path.join(source_folder, matching_image)
                destination_image_path = os.path.join(destination_folder, split, 'images', matching_image)
                shutil.copy(image_path, destination_image_path)

                # Copy label
                label_path = os.path.join(label_split_folder, label_file)
                destination_label_path = os.path.join(destination_folder, split, 'labels', label_file)
                shutil.copy(label_path, destination_label_path)

                print(f"Copied {matching_image} and {label_file} to {split} folder")
            else:
                print(f"No matching image found for label file {label_file}")

# Apply function for each split
for split in ['train', 'valid', 'test']:
    copy_files_with_matching_time(split)

print("Files copied successfully!")