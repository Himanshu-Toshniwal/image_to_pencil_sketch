

# # pip install opencv-python

import cv2

image = cv2.imread("toshu.jpg")  # Corrected the assignment operator

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inverted = 255 - gray_image  # Added the assignment operator here

blur = cv2.GaussianBlur(inverted, (21, 21), 0)

invertedblur = 255 - blur

sketch = cv2.divide(gray_image, invertedblur, scale=256.0)  # Corrected the assignment operator

cv2.imwrite("sketch_image.png", sketch)

# Add these lines for full-size display
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)  # Create resizable window
cv2.resizeWindow("Image", 800, 600)  # Adjust window size (optional)

cv2.imshow("Image", sketch)

cv2.waitKey(0)  # Keep the image window open until a key is pressed
cv2.destroyAllWindows()  # Close the window


