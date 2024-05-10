import cv2
import numpy as np
import os

# Function to draw rectangles on an image


def draw_rectangles(image_path, coordinates):
    # Read the image
    image = cv2.imread(image_path)

    # Iterate over each set of coordinates
    for coords in coordinates:
        # Split the string and extract x, y, w, h values
        coord_parts = coords.split()
        if len(coord_parts) >= 8:
            try:
                x = int(coord_parts[1])
                y = int(coord_parts[3])
                w = int(coord_parts[5])
                h = int(coord_parts[7])
                # Draw rectangle on the image
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            except ValueError:
                print(f"Invalid coordinates format: {coords}")
        else:
            print(f"Invalid coordinates format: {coords}")

    # Save the image with rectangles to the test folder
    output_folder = './test'
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Image with rectangles saved to: {output_path}")


# Function to process all text files in a directory
def process_text_files(folder_path):
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            # Read coordinates from the text file
            coordinates = []
            with open(os.path.join(folder_path, file_name), 'r') as file:
                for line in file:
                    coordinates.append(line.strip())

            # Load the corresponding image and draw rectangles
            image_name = file_name.replace('.txt', '.png')
            image_path = os.path.join(folder_path, image_name)
            if os.path.exists(image_path):
                draw_rectangles(image_path, coordinates)
            else:
                print(f"Image not found for coordinates in file: {file_name}")


# Path to the folder containing text files
folder_path = './sample_original'

# Process all text files in the folder
process_text_files(folder_path)
