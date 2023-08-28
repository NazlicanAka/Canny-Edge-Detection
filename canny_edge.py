import numpy as np
import cv2 as cv


def change_edge_detection(x):
    edges = cv.Canny(img, 100, x)  # second and the third arguments are thresholds.
    cv.imshow('Edge Image', edges)


img = cv.imread('assets_opencv/messi.png', cv.IMREAD_GRAYSCALE)

assert img is not None, "file could not be read, check with os.path.exists()"

cv.namedWindow('image')
cv.imshow('Original Image', img)

cv.createTrackbar('color_track', 'image', 100, 400, change_edge_detection)

cv.waitKey(0)
cv.destroyAllWindows()
