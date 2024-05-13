
import pytesseract
from PIL import Image


class TesseractEngine():
    # Input : image file path (str), oem (int)(0-3), psm (int)(0-12), language (str)("eng+tha")
    # Output : boxes_data
    # For : get bounding boxes from TESSERACT
    def tesseract_bounding_box(self, image_path, oem, psm, languages):
        image = Image.open(image_path)
        boxes_data = pytesseract.image_to_boxes(
            image, lang=languages, config=f'--oem {oem} --psm {psm}')

        return boxes_data
