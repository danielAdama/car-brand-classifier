from flask import Flask, request, jsonify
import os
import cv2
import io
import base64
import sys
sys.path.append(r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier')
from config import config
# from yolo_detect_images import detectObj
# sys.path.append(r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier')
from detector.car import CarDetector
from PIL import Image, ImageFile
import numpy as np
import imutils


app = Flask(__name__)
os.environ['FLASK_DEBUG']="development"
cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')


@app.route("/v1/detect-obj", methods=["POST"])
def detect():

    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        np_array_encode = np.fromstring(img, np.uint8)
    
    # if request.files.get("image"):
    # image_file = request.files['image']
    # img = Image.open(io.BytesIO(image_file.read()))
    # img.load()

    return jsonify({"msg":[img.width, img.height]})

if __name__ == "__main__":
    app.run(debug=True, port=8080)