import cv2
import numpy as np
import matplotlib.pyplot as plt

def enhance_and_display_nir_image(image_path, cmap='gist_stern', gamma=1):
    # Load the image using OpenCV in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Unable to load image")
        return

    # Normalize the image to enhance visibility
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(normalized_image)

    # Apply gamma correction
    gamma_corrected_image = np.array(255 * (clahe_image / 255) ** gamma, dtype='uint8')

    # Display the original and enhanced images side by side using Matplotlib
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original NIR Image')
    plt.axis('off')  # Hide axes for better visualization

    # Enhanced Image
    plt.subplot(1, 2, 2)
    plt.imshow(gamma_corrected_image, cmap=cmap)
    plt.title(f'Enhanced NIR Image with {cmap} colormap')
    plt.axis('off')  # Hide axes for better visualization

    plt.show()

     # Print pixel value statistics for the original image
    print("Original Image Statistics:")
    print(image)
    #print(f"Min: {image.min()}, Max: {image.max()}, Mean: {image.mean():.2f}, Std: {image.std():.2f}")

    # Print pixel value statistics for the enhanced image
    print("Enhanced Image Statistics:")
    print(gamma_corrected_image)
    #print(f"Min: {gamma_corrected_image.min()}, Max: {gamma_corrected_image.max()}, Mean: {gamma_corrected_image.mean():.2f}, Std: {gamma_corrected_image.std():.2f}")
    
# Example usage
# image_path = r'C:\Users\Nicholas\Documents\Uni\Github\part-4-project\ebus-multisource-camera-main\NIR\leaves_20240620T15_40_00_835412Z.png'  # Use raw string for the path
image_path = ...
enhance_and_display_nir_image(image_path, cmap='gst_stern')