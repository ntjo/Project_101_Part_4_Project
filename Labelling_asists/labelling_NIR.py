import os
import shutil

# THIS CODE APPLIES LABELS OF RGB IMAGES FROM ROBOFLOW TO THE CORRESPONDING NIR
# IMAGES, AND GENERATES A NEW FOLDER CONTAINING THE MATCHING PHOTOS SPLIT & LABELS

# ADD NIR LABELS

# plain RGB images folder from Google Drive
source_folder = '/Users/ray/Downloads/NIR_ambient_day'

# new folder created by yourself
destination_folder = '/Users/ray/Desktop/ambient_day_NIRonly'

# roboflow's folder, pre labelled ambient RGB in train, test and valid folders
label_folder = '/Users/ray/Downloads/project-101-disease-detection.v36-21-9-24-daytime-65images.yolov8'

# Create folder structure
for split in ['valid', 'train', 'test']:
    os.makedirs(os.path.join(destination_folder, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(destination_folder, split, 'labels'), exist_ok=True)

# Function to copy images and labels
def copy_files(split):
    label_split_folder = os.path.join(label_folder, split, 'labels')
    for label_file in os.listdir(label_split_folder):
        if label_file.endswith('.txt'):
            # Extract the base name of the image
            image_base = label_file.split('_png')[0] + '.png'
            # Copy image
            image_path = os.path.join(source_folder, image_base)
            if os.path.exists(image_path):
                shutil.copy(image_path, os.path.join(destination_folder, split, 'images', image_base))
            # Adjust label file name
            new_label_file = label_file.split('_png')[0] + '.txt'
            # Copy label with new name
            shutil.copy(os.path.join(label_split_folder, label_file), os.path.join(destination_folder, split, 'labels', new_label_file))

# Copy files for each split
for split in ['train', 'valid', 'test']:
    copy_files(split)

print("Files copied successfully!")
