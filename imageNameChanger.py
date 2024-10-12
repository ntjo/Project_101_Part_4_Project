import os

def rename_images(folder_A, folder_B):
    # Get a sorted list of file names from both folders
    files_A = sorted(os.listdir(folder_A))
    files_B = sorted(os.listdir(folder_B))
    
    # Ensure both folders have the same number of files
    if len(files_A) != len(files_B):
        print("The number of files in both folders is not the same.")
        return
    
    # Loop through files and rename them
    for file_A, file_B in zip(files_A, files_B):
        # Construct full file paths for folder B
        old_file_path_B = os.path.join(folder_B, file_B)
        new_file_name_B = file_A  # The new name from folder A
        new_file_path_B = os.path.join(folder_B, new_file_name_B)
        
        # Rename the file in folder B
        os.rename(old_file_path_B, new_file_path_B)
        print(f"Renamed {file_B} to {new_file_name_B}")

# Example usage
folder_A = "D:/Downloads/day_21_9_24/LED/day_21_9_24_NIR_LEDXLED/NIR"  # Replace with your actual folder A path
folder_B = "D:/Downloads/day_21_9_24/LED/day_21_9_24_NIR_FloodXLED/NIR"  # Replace with your actual folder B path

rename_images(folder_A, folder_B)
