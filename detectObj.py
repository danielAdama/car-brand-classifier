import cv2
import numpy as np
import os
import time
from config import config
import imutils
from imutils import paths
from detector.car import CarDetector

cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')
images = list(paths.list_images(config.EXAMPLE_IMGS))
t1 = time.time()
for image in images:
    image_name = image.split(os.path.sep)[-1].split('.')[0]
    image_format = image.split(os.path.sep)[-1].split('.')[1]
    print(f"Processing Image: '{image_name}' with format {image_format}")
    # Convert the input image resize it to have a width of 900px (to speedup processing) 
    image = cv2.imread(image)
    frame = imutils.resize(image, 900)
    (height, width) = frame.shape[:2]
    image = cv2.resize(image, (width, height))
    scores, boxes = cd.vehicle_detected(image)
    t2 = time.time()
    print(f"time: {t2-t1:.4f} secs")
    for score, box in zip(scores, boxes):
        x, y, w, h = box
        cx = int((x + x + w)/2)
        cy = int((y + y + h)/2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        cv2.rectangle(frame, (719, 5), (489, 39), (0, 255, 0), -1)
        cv2.putText(frame, f"Car Detected", (494, 30), config.FONT, 1, (240, 135, 87), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(score), (x, y-5), config.FONT, 0.8, (0, 255, 0), 1)
        
    cv2.imshow('Car Classifier', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#     if len(boxes) > 0:
#         print(boxes.flatten())