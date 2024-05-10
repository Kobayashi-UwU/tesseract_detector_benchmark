'''
funtion to draw rectangle on image to find x y w h from rectangle drew
'''

import cv2

drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow('image', img)
        print("x:", ix, "y:", iy, "w:", x - ix, "h:", y - iy)


# Load an image
img = cv2.imread('./sample_original/eng_01.png')

# Create a window and bind the function to the window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# Display the image and wait for a key press
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
