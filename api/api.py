import argparse
from flask import Flask, request, jsonify
import os
import pandas as pd
import sys
sys.path.append(os.getcwd())
from config import config
from yolo_detect_images import detectObject


app = Flask(__name__)
# os.environ['FLASK_DEBUG']="development"
app.config['FLASK_DEBUG']="development"


@app.route("/v1/image", methods=["POST"])
def detect_image():

    if not request.method == "POST":
        return
    
    if request.files.get("image"):
        image_file = request.files["image"]
        result = detectObject(image_file)
        return pd.Series(result).to_json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Car Classifier Api exposing YOLOv4")
    parser.add_argument("-p", "--port", default=8080, type=int, help="port number")
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)