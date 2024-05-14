import cv2
import numpy as np


def draw_boxes_on_image(image_path, boxes_data):
    # Read the image
    image = cv2.imread(image_path)

    # Iterate through each bounding box data
    for box in boxes_data:
        left, top, width, height, conf, text = box

        # Convert coordinates to integers
        left, top, width, height = int(left), int(top), int(width), int(height)

        # Draw bounding box rectangle
        cv2.rectangle(image, (left, top), (left + width,
                      top + height), (0, 255, 0), 2)

    return image


# Example usage
data = [[58, 43, 38, 40, 31, '®'], [138, 45, 164, 29, 82, 'ChatGPT'], [140, 110, 20, 29, 82, 'It'], [170, 118, 115, 21, 95, 'seems'], [
    295, 110, 69, 29, 96, 'that'], [374, 110, 56, 29, 96, 'the'], [441, 110, 100, 36, 67, 'script'], [553, 110, 25, 29, 56, 'is']]

# Assuming 'image.jpg' is your image file
image_with_boxes = draw_boxes_on_image(
    './groundtruth/sample_original/eng_02.png', data)

# Display or save the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image_with_boxes)
cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to save the image
# cv2.imwrite('image_with_boxes.jpg', image_with_boxes)
