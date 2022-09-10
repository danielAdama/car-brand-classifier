from pyexpat import model
from turtle import width
import cv2
import imutils
import time
import numpy as np
from config import config
from detector.car import CarDetector

# Load the model
car = CarDetector()

webcam = cv2.VideoCapture(config.VIDEO)
time.sleep(2.0)
if (webcam.isOpened == False):
    print("\nUnable to read video")


while True:
    success, frame = webcam.read()
    if success == True:
        frame = imutils.resize(frame, 700)
        (height, width) = frame.shape[:2]

        cv2.imshow("Live", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        break