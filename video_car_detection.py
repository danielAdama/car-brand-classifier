import cv2
import imutils
import time
import numpy as np
from config import config
from detector.car import CarDetector

# Load the model
cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')
webcam = cv2.VideoCapture(config.VIDEO)
time.sleep(2.0)
if (webcam.isOpened == False):
    print("\nUnable to read video")

while True:
    success, frame = webcam.read()
    if success == True:
        frame = imutils.resize(frame, 700)
        (height, width) = frame.shape[:2]
        frame = cv2.resize(frame, (width, height))
        boxes = cd.vehicle_detected(frame)
        for box in boxes:
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Live", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        break