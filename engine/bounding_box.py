import subprocess
import cv2
import os
import pytesseract
from PIL import Image


class BoundingBox():

    # Input : image file path (str), oem (int)(0-3), psm (int)(0-12), language (str)("eng+tha")
    # Output : boxes_data
    # For : get bounding boxes from TESSERACT
    def get_tesseract_bounding_box(self, image_path, oem, psm, languages):
        image = Image.open(image_path)
        boxes_data = pytesseract.image_to_boxes(
            image, lang=languages, config=f'--oem {oem} --psm {psm}')

        return boxes_data

    # Input : image, boxes_data
    # Output : return image
    # For : draw texts bounding box from TESSERACT
    def draw_tesseract_bounding_box(self, img_cv, boxes_data):
        for box_data in boxes_data.splitlines():
            box = box_data.split(' ')
            x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
            cv2.rectangle(
                img_cv, (x, img_cv.shape[0] - y), (w, img_cv.shape[0] - h), (0, 255, 0), 2)

        return img_cv

        # Input : image file path (str), oem (int)(0-3), psm (int)(0-12), language (str)("eng+tha")
        # Output : return image
        # For : draw texts bounding box on TESSERACT output
        # OEM working list : 1 3
        # PSM working list : 1 3 4 5 6 7 8 9 10 11 12
    def run_tesseract(self, image_path, oem, psm, languages):
        boxes_data = self.get_tesseract_bounding_box(
            image_path, oem, psm, languages)

        # Convert image to OpenCV format
        img_cv = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        result_image = self.draw_tesseract_bounding_box(img_cv, boxes_data)

        return result_image

    # Input : image file path (str), coordinates array [x, y, w, h] (int)
    # Output : return image
    # For : draw rectangle from coordinates array
    def draw_rectangles(self, image_path, coordinates):
        image = cv2.imread(image_path)

        for coords in coordinates:
            coord_parts = coords.split()
            if len(coord_parts) >= 8:
                try:
                    x = int(coord_parts[1])
                    y = int(coord_parts[3])
                    w = int(coord_parts[5])
                    h = int(coord_parts[7])
                    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
                except ValueError:
                    print(f"Invalid coordinates format: {coords}")
            else:
                print(f"Invalid coordinates format: {coords}")

        return image

    # Input : image file path (str)
    # Output : return image
    # For : draw bounding boxes from ground truth
    def draw_boxes_from_groundtruth(self, image_path):
        coordinates = []
        groundtruth = image_path.replace('.png', '.txt')

        with open(groundtruth, 'r') as file:
            for line in file:
                coordinates.append(line.strip())

        if os.path.exists(image_path):
            result_image = self.draw_rectangles(image_path, coordinates)
        else:
            print(f"Image not found for coordinates in file: {image_path}")

        return result_image

    # Input : tesseract_output file path (str)
    # Output : percentage of correct boxes (int)
    # For : calculate percentage between groundtruth and tesseract boxes
    def calculate_correctness(self, tesseract_output, groundtruth):
        return 100

    # Input : image file path (str), oem (int)(0-3), psm (int)(0-12)
    # Output : return image
    # For : draw both groundtruth and tesseract boxes to see differentness
    def draw_both_boxes(self, image_path, oem, psm, languages):
        result_image = self.draw_boxes_from_groundtruth(image_path)
        boxes_data = self.get_tesseract_bounding_box(
            image_path, oem, psm, languages)
        result_image = self.draw_tesseract_bounding_box(
            result_image, boxes_data)

        return result_image
