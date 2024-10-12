from pathlib import Path
import os
import numpy as np
import cv2
import shutil

def merge_rgb_nir(rgb_path: Path, nir_path: Path):
    ## Store images paths for both rgb and nir
    images = {}

    def get_img_key(file_name: str, is_nir: bool):
        if is_nir:
            return file_name.split('.')[0]
        else:
            return file_name.split('_png')[0]

    for file in os.listdir(rgb_path):
        key = get_img_key(file, False)
        if key not in images:
            images[key] = []
        images[key].append((rgb_path / file).resolve())

    for file in os.listdir(nir_path):
        key = get_img_key(file, True)
        if key not in images:
            continue
        images[key].append((nir_path / file).resolve())

    for image_list in images.values():
        # Ensure both RGB and NIR images are present
        if len(image_list) < 2:
            print(f"Warning: Missing corresponding NIR image for {image_list[0]}. Skipping this pair.")
            continue

        rgb_img = cv2.imread(str(image_list[0]))
        nir_img = cv2.imread(str(image_list[1]))

        # Ensure the images were read correctly
        if rgb_img is None or nir_img is None:
            print(f"Error: Could not read image {image_list[0]} or {image_list[1]}. Skipping.")
            continue

        nir_img = cv2.cvtColor(nir_img, cv2.COLOR_BGR2GRAY)

        img = np.concatenate((rgb_img, nir_img[..., np.newaxis]), axis=2)

        np.save(str(image_list[0]).replace(".jpg", ".npy"), img)
        os.remove(image_list[0])

def duplicate_folder(src: Path, dest: Path):
    # Check if the destination folder already exists
    if dest.exists():
        print(f"Folder {dest} already exists. Skipping duplication.")
        return
    try:
        shutil.copytree(src, dest)
        print(f"Folder {src} successfully duplicated to {dest}.")
    except Exception as e:
        print(f"Error duplicating folder {src} to {dest}: {e}")

def get_images_labels(dir: Path, res: dict):
    for subdir in ["images", "labels"]:
        for file in os.listdir(dir / subdir):
            key = file.split('rf')[0]

            if key not in res:
                res[key] = []

            res[file.split('rf')[0]].append((dir / subdir / file).resolve())

    return res

if __name__ == "__main__":
    ## The location of the dataset that contains 'data.yaml', 'train' and 'valid' folders
    dataset_location = Path("/content/project-101-disease-detection-57").resolve()

    ## The location that stores all the NIR images with the same name as the dataset images
    NIR_DIR = Path("/content/night/led/led").resolve()

    ## Duplicate the original dataset folder to avoid modifying the original
    duplicated_dataset_location = Path("/content/night_20_9_24_merged_ledXled").resolve()
    duplicate_folder(dataset_location, duplicated_dataset_location)

    ## Perform the image merging on the duplicated folder
    merge_rgb_nir(duplicated_dataset_location / "train" / "images", NIR_DIR)
    merge_rgb_nir(duplicated_dataset_location / "valid" / "images", NIR_DIR)
