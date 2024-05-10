import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image


def extract_boxes_tess(data):
    bounding_boxes = []
    for line in data.split('\n'):
        if line.strip():  # Skip empty lines
            parts = line.split()
            char = parts[0]
            x1, y1, x2, y2 = map(int, parts[1:5])
            x1, y1, x2, y2 = (x1, -y2, x2, -y1)
            bounding_boxes.append((x1, y1, x2, y2))
    return bounding_boxes


def read_coordinates_from_file(file_path):
    # Initialize an empty list to store the tuples
    coordinates = []

    # Open the text file
    with open(file_path, 'r') as file:
        # Read each line
        for line in file:
            # Split the line by whitespace
            parts = line.split()
            # Extract x, y, w, and h values
            x1 = int(parts[1])
            y1 = int(parts[3])
            w = int(parts[5])
            h = int(parts[7])
            # Calculate x2 and y2
            x2 = x1 + w
            y2 = y1 + h
            # Append the tuple (x1, y1, x2, y2) to the list
            coordinates.append((x1, y1, x2, y2))

    # Return the list of tuples
    return coordinates


image_path = './groundtruth/sample_original/eng_01.png'
groundtruth = image_path.replace('.png', '.txt')

with Image.open(image_path) as img:
    width, height = img.size

rows = height
columns = width

# Create a 2D array filled with zeroes
array_2d = [[0 for _ in range(columns)] for _ in range(rows)]

# Define OCR Engine Mode (OEM), Page Segmentation Mode (PSM), and language
oem = 3  # LSTM OCR Engine Mode (OEM)
psm = 4  # Fully automatic page segmentation mode (PSM)
language = 'eng'  # English language

# Open an image
image = Image.open(image_path)

# Get bounding boxes
boxes_data = pytesseract.image_to_boxes(
    image, lang=language, config=f'--oem {oem} --psm {psm}')

# Extract bounding boxes
bounding_boxes = extract_boxes_tess(boxes_data)


# Label pixels within the bounding boxes as 1
for x1, y1, x2, y2 in bounding_boxes:
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            array_2d[i][j] = 1


bounding_boxes = read_coordinates_from_file(groundtruth)

# Label pixels within the bounding boxes as 1
for x1, y1, x2, y2 in bounding_boxes:
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if array_2d[i][j] >= 1:
                array_2d[i][j] = 2
            else:
                array_2d[i][j] = 1

# Convert the 2D array into a numpy array for plotting
image_array = np.array(array_2d)

# Plot the image
plt.imshow(image_array, cmap='gray')
plt.axis('off')
plt.show()

# count_sum = 0
# count_two = 0
# for i in range(rows):
#     for j in range(columns):
#         if array_2d[i][j] == 1:
#             count_sum += 1
#         if array_2d[i][j] == 2:
#             count_two += 1
#             count_sum += 1
# print(count_sum, count_two)
# print((count_two/count_sum) * 100)
