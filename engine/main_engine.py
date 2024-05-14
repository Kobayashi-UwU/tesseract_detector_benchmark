import cv2
from engine.bounding_box_engine import BoundingBoxEngine
from engine.tesseract_engine import TesseractEngine


class MainEngine():
    def run_tesseract(self, image_path, oem, psm, languages):
        boxes_data = TesseractEngine().tesseract_bounding_box(
            image_path, oem, psm, languages)

        # Convert image to OpenCV format
        img_cv = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        result_image = BoundingBoxEngine().draw_tesseract_bounding_box(
            img_cv, boxes_data)

        tess_box_text = TesseractEngine().extract_text_tesseract(boxes_data)
        return result_image, tess_box_text

    # Input : image file path (str), oem (int)(0-3), psm (int)(0-12)
    # Output : return image
    # For : draw both groundtruth and tesseract boxes to see differentness
    def draw_both_boxes(self, image_path, oem, psm, languages):
        result_image = BoundingBoxEngine().draw_boxes_from_groundtruth(
            image_path)
        boxes_data = TesseractEngine().tesseract_bounding_box(
            image_path, oem, psm, languages)
        result_image = BoundingBoxEngine().draw_tesseract_bounding_box(
            result_image, boxes_data)

        return result_image

    def run_tesseract_con(self, image_path, oem, psm, languages, confidence_treshold):
        data = TesseractEngine().tesseract_bounding_boxes_confidence(
            image_path, oem, psm, languages)

        bounding_box = TesseractEngine().extract_tess_data(data)

        result_image = BoundingBoxEngine().draw_boxes_on_image(
            image_path, bounding_box, confidence_treshold)

        tess_con_box_text = TesseractEngine().extract_text_tesseract_data(data)

        return result_image, tess_con_box_text
