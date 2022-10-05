import cv2
import numpy as np
import os
import io
from PIL import Image
import sys
sys.path.append(r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier')
from config import config
import imutils
from detector.car import CarDetector

def detectObject(image_file):

    cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')
    image_bytes = image_file.read()
    img = np.array(Image.open(io.BytesIO(image_bytes)).convert('RGB'))
    
    # Convert RGB to BGR 
    cv_image = img[:, :, ::-1].copy()
    frame = imutils.resize(cv_image, 900)
    (height, width) = frame.shape[:2]
    image = cv2.resize(cv_image, (width, height))
    scores, boxes = cd.vehicle_detected(image)

    output = {}

    if len(boxes) > 0:
        output['detections'] = {}
        output['detections']['prediction'] = []
        for score, box in zip(scores, boxes):
            detection = {}
            x, y, w, h = box
            label = 'Car'

            detection['Label'] = label
            detection['Confidence'] = score
            detection['X'] = x
            detection['Y'] = y
            detection['Width'] = w
            detection['Height'] = h
            output['detections']['prediction'].append(detection)
    else:
        output['detections'] = "No Car detected"

    return output