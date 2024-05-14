
import pytesseract
from PIL import Image


class TesseractEngine():
    # Input : image file path (str), oem (int)(0-3), psm (int)(0-12), language (str)("eng+tha")
    # Output : boxes_data
    # For : get bounding boxes from TESSERACT
    def tesseract_bounding_box(self, image_path, oem, psm, languages):
        image = Image.open(image_path)
        boxes_data = pytesseract.image_to_boxes(
            image, lang=languages, config=f'--oem {oem} --psm {psm} -l {languages}')

        return boxes_data

    def tesseract_bounding_boxes_confidence(self, image_path, oem, psm, languages):
        # Load the image
        image = Image.open(image_path)

        custom_config = f'--oem {oem} --psm {psm} -l {languages}'

        # Get OCR data with custom configuration
        data = pytesseract.image_to_data(
            image, output_type=pytesseract.Output.DICT, config=custom_config)

        return data

    def extract_tess_data(self, data):
        result = []
        # Extract and print all the available data
        num_boxes = len(data['level'])
        for i in range(num_boxes):
            # level = data['level'][i]
            # page_num = data['page_num'][i]
            # block_num = data['block_num'][i]
            # par_num = data['par_num'][i]
            # line_num = data['line_num'][i]
            # word_num = data['word_num'][i]
            left = data['left'][i]
            top = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            conf = data['conf'][i]
            text = data['text'][i]

            result.append([left, top, width, height, conf, text])

        return result

    def extract_text_tesseract(self, boxes_data):
        result = ""
        for box_data in boxes_data.splitlines():
            box = box_data.split(' ')
            text = box[0]
            result += f"{text}"

        return result

    def extract_text_tesseract_data(self, data):
        result = ""
        # Extract and print all the available data
        num_boxes = len(data['level'])
        for i in range(num_boxes):
            text = data['text'][i]
            result += f"{text}"
            result += " "
        return result
