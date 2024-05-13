import numpy as np
from PIL import Image

from engine.tesseract_engine import TesseractEngine


class IouEngine():
    def extract_boxes_tess(self, data):
        bounding_boxes = []
        for line in data.split('\n'):
            if line.strip():  # Skip empty lines
                parts = line.split()
                char = parts[0]
                x1, y1, x2, y2 = map(int, parts[1:5])
                x1, y1, x2, y2 = (x1, -y2, x2, -y1)
                bounding_boxes.append((x1, y1, x2, y2))
        return bounding_boxes

    def read_coordinates_from_file(self, file_path):
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

    def runiou(self, image_path, oem, psm, language):
        with Image.open(image_path) as img:
            width, height = img.size

        rows = height
        columns = width

        array_2d = [[0 for _ in range(columns)] for _ in range(rows)]

        boxes_data = TesseractEngine().tesseract_bounding_box(
            image_path, oem, psm, language)

        # Extract bounding boxes
        bounding_boxes = self.extract_boxes_tess(boxes_data)

        # Label pixels within the bounding boxes as 1
        for x1, y1, x2, y2 in bounding_boxes:
            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    array_2d[i][j] = 1

        groundtruth = image_path.replace('.png', '.txt')

        bounding_boxes = self.read_coordinates_from_file(groundtruth)

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

        count_sum = 0
        count_two = 0
        for i in range(rows):
            for j in range(columns):
                if array_2d[i][j] == 1:
                    count_sum += 1
                if array_2d[i][j] == 2:
                    count_two += 1
                    count_sum += 1

        # Define a color map
        color_map = {
            0: (0, 0, 0),   # black
            1: (255, 255, 255),   # white
            2: (255, 0, 0)   # red
        }

        # Convert the 2D array to a NumPy array with dtype=uint8
        image_array = np.array([[color_map[value] for value in row]
                                for row in array_2d], dtype=np.uint8)

        # Create a PIL Image object from the NumPy array
        image_iou = Image.fromarray(image_array)

        return (count_two/count_sum) * 100, image_iou
