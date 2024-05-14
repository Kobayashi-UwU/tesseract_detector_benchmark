from PIL import Image

# Example image path
image_path = './groundtruth/sample_original/tha_01.png'

# Load the image
image = Image.open(image_path)

# Define bounding boxes based on your data
bounding_boxes = [
    (0, 0, 292, 122),
    (60, 35, 60 + 158, 35 + 35),
    (60, 35, 60 + 158, 35 + 35),
    (60, 35, 60 + 158, 35 + 35),
    (55, 40, 65 + 18, 50 + 25),
    (77, 31, 77 + 16, 31 + 49),
    (92, 35, 92 + 16, 35 + 35),
    (108, 45, 108 + 16, 45 + 25),
    (128, 35, 128 + 11, 35 + 35),
    (138, 31, 138 + 16, 31 + 49),
    (154, 47, 154 + 16, 47 + 23),
    (169, 31, 169 + 16, 31 + 49),
    (184, 35, 184 + 15, 35 + 35),
    (199, 47, 199 + 19, 47 + 23),
]

# Crop the image for each bounding box
cropped_images = []
for i, box in enumerate(bounding_boxes):
    left, top, right, bottom = box
    cropped_image = image.crop((left, top, right, bottom))

    # Convert the image to RGB if it's in RGBA mode
    if cropped_image.mode == 'RGBA':
        cropped_image = cropped_image.convert('RGB')

    cropped_images.append(cropped_image)
    cropped_image.save(f'cropped_image_{i}.jpg')

print(f'{len(cropped_images)} images cropped and saved.')
