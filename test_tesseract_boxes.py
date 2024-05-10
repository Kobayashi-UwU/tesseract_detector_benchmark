import pytesseract
from PIL import Image
import cv2

# Path to your Tesseract executable (if not in your PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 11 13 14 15 16 17 18 19 110 111 112 31 33 34 35 36 37 38 39 310 311 312
# Define OCR Engine Mode (OEM), Page Segmentation Mode (PSM), and language
oem = 3  # LSTM OCR Engine Mode (OEM)
psm = 4  # Fully automatic page segmentation mode (PSM)
language = 'eng'  # English language

# Open an image
image_path = './groundtruth/sample_original/eng_03.png'
image = Image.open(image_path)

# Get bounding boxes
boxes_data = pytesseract.image_to_boxes(
    image, lang=language, config=f'--oem {oem} --psm {psm}')

# # Convert image to OpenCV format
# img_cv = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

# # Draw bounding boxes on the image
# for box_data in boxes_data.splitlines():
#     box = box_data.split(' ')
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(
#         img_cv, (x, img_cv.shape[0] - y), (w, img_cv.shape[0] - h), (0, 255, 0), 2)

# # Display the image with bounding boxes
# cv2.imshow('Bounding Boxes', img_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(boxes_data)
