import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of skin color in HSV
    scaleSatLower = 0.28
    scaleSatUpper = 0.68

    lower_blue = np.array([0, scaleSatLower * 255, 0])
    upper_blue = np.array([25, scaleSatUpper * 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv.destroyAllWindows()