import cv2
import numpy as np
import matplotlib.pyplot as plt

cap= cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,100,200)
    laplacian= cv2.Laplacian(gray, cv2.CV_64F)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imshow('swarnima', frame)
    cv2.imshow('somethingWEIRD', laplacian)
    cv2.imshow('x', sobelx)
    cv2.imshow('y', sobely)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


