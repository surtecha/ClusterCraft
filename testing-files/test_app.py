import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances

# Custom algorithm
from kmeans_v2 import CustomKMeans as ckm

def list_image_files(folder_path):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    image_files = [file for file in os.listdir(folder_path) if os.path.splitext(file)[1].lower() in image_extensions]
    return image_files

def segment_image(selected_image_path):
    image = plt.imread(selected_image_path)

    plt.figure(figsize=(10, 5))
    plt.title('Original Image')
    plt.imshow(image)
    plt.show()

    num_clusters = int(input("\nNumber of clusters (more than 5 and less than 15): "))    

    print("\nSegmenting the image using Custom KMeans...\n")

    # Custom segmentation
    n_pixels = image.shape[0] * image.shape[1]
    image_pixels = image.reshape(n_pixels, -1)

    custom_start = time.time()
    kmeans_custom = ckm(n_clusters=num_clusters)
    kmeans_custom.fit(image_pixels)
    cluster_labels = kmeans_custom.predict(image_pixels)
    segmented_img_2 = kmeans_custom.centroids[cluster_labels].reshape(image.shape)
    custom_end = time.time()

    plt.figure(figsize=(10, 5))

    # Original image
    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis('on')

    # Segmentation using custom KMeans
    plt.subplot(122)
    plt.title("Segmentation (custom KMeans)")
    plt.imshow(segmented_img_2.astype(np.uint8))
    plt.axis('on')

    # Adjust spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()

    print(f"Custom KMeans took {custom_end - custom_start} seconds.\n")

images_folder = 'C:/Users/teja1/Downloads'
image_files = list_image_files(images_folder)

print("Available image files in the Downloads folder:")
for idx, file in enumerate(image_files, start=1):
    print(f"{idx}. {file}")

selected_index = int(input("Enter the index of the image to perform segmentation on: ")) - 1

if 0 <= selected_index < len(image_files):
    selected_image_path = os.path.join(images_folder, image_files[selected_index])
    print(f"Selected image: {selected_image_path}")
    segment_image(selected_image_path)
else:
    print("Invalid index.")
