import cv2
import os


class BoundingBoxEngine():

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
