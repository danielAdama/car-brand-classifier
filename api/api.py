import time
from flask import Flask, request, jsonify
import os
import cv2
import io
import json
import pandas as pd
import sys
sys.path.append(r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier')
from config import config
# from yolo_detect_images import detectObj
# sys.path.append(r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier')
from detector.car import CarDetector
from PIL import Image, ImageFile
import numpy as np
import imutils

t1 = time.time()
app = Flask(__name__)
os.environ['FLASK_ENV']="development"
cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')


@app.route("/v1/detect-obj", methods=["POST"])
def detect():

    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = np.array(Image.open(io.BytesIO(image_bytes)).convert('RGB'))
        t2 = time.time()
        print(t2-t1)
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
        # t2 = time.time()
        # print(t2-t1)
    return pd.Series(output).to_json(), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)