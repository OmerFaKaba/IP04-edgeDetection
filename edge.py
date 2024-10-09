import cv2
import matplotlib.pyplot as plt
import numpy as np

# Function to display an image with a title
def imshow_img(img, title):
    plt.figure(), plt.imshow(img), plt.title(title)

img = cv2.imread("anitkabir.jpg", 0) # Read the image in grayscale mode
imshow_img(img, "original") # Display the original image

edges = cv2.Canny(image=img, threshold1=0, threshold2=255) # Apply Canny edge detection
imshow_img(edges, "edges") # Display the edges detected in the image

plt.show()