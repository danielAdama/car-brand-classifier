import argparse
from functools import wraps
from flask import Flask, request, jsonify
import os
import pandas as pd
import sys
import jwt
sys.path.append(os.getcwd())
from config import config
from yolo_detect_images import detectObject


app = Flask(__name__)
app.config['FLASK_DEBUG']="development"
app.config['SECRET_KEY']=config.KEYS["SECRET_KEY"]
app.config['USER_NAME']=config.KEYS["USER_NAME"]


def token_required(f):
    @wraps
    def decorated(*args, **kwargs):
        token = None
        access = 'access-token'
        if access in request.headers:
            token = request.headers[access]

        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return {
                "message": "Invalid Authentication Token",
                "data": None,
                "error": "Unauthorized"
            }

        return f(*args, **kwargs)
    return decorated

@app.route("/v1/login", methods=["POST"])
def login():
    auth = request.json
    if not auth:
        return {
            "message": "Please provide user details",
            "data": None,
            "error": "Bad request"
        },400
    
    if auth['SECRET_KEY'] == app.config['SECRET_KEY'] and auth['USER_NAME'] == app.config['USER_NAME']:
        # if a user is successfullly loggedin return the token
        try:
            token = jwt.encode({'user':app.config["USER_NAME"]}, app.config['SECRET_KEY'])
            return {
                "message": "Successfully fetched authentication token",
                "user": app.config['USER_NAME'],
                "token":token
            },200
        except Exception as e:
            return {
                "error":"Something went wrong",
                "message":str(e)
            }




@app.route("/v1/image", methods=["POST"])
# @token_required
def detect_image():

    if not request.method == "POST":
        return {
            "message": "Please provide image",
            "data": None,
            "error": "Bad request"
        },400
    
    if request.files.get("image"):
        image_file = request.files["image"]
        result = detectObject(image_file)
        return pd.Series(result).to_json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Car Classifier Api exposing YOLOv4")
    parser.add_argument("-p", "--port", default=8080, type=int, help="port number")
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)