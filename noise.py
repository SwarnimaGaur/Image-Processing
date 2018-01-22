import cv2
import numpy as np
import matplotlib as plt

cap= cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    #cv2.imshow('original', frame)
    noise = np.random.randint(5, size = (frame.shape[0], frame.shape[1], 1))
    frame = np.where(noise ==0, 0, frame)
    frame = np.where(noise ==5, 1, frame)
    cv2.imshow('noise', frame)

    blur = cv2.GaussianBlur(frame, (5,5), 0)
    median = cv2.medianBlur(frame, 5)
    cv2.imshow('median', median)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destoryAllWindows()
