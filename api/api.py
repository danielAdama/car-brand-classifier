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
from yolo_detect_images import detectObject
from PIL import Image
import numpy as np
import imutils

app = Flask(__name__)
os.environ['FLASK_DEBUG']="development"


@app.route("/v1/image", methods=["POST"])
def detect():

    if not request.method == "POST":
        return
    
    if request.files.get("image"):
        image_file = request.files["image"]
        result = detectObject(image_file)
    return pd.Series(result).to_json(), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)