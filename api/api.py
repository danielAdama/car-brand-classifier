import argparse
from functools import wraps
from flask import Flask, request, jsonify
import os
import pandas as pd
import json
import jwt
import sys
sys.path.append(os.getcwd())
from config import config
from yolo_detect_images import detectObject


app = Flask(__name__)
app.config['FLASK_DEBUG']="development"
app.config['SECRET_KEY']=config.KEYS["SECRET_KEY"]
app.config['USER_NAME']=config.KEYS["USER_NAME"]


def token_required(f):
    @wraps(f)
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
            }, config.HTTP_403_UNAUTHORIZED
        
        try:
            data = jwt.decode(
                token, 
                app.config['SECRET_KEY'], 
                algorithms=["HS512"]
            )
        except:
            return {
                "message": "Invalid Authentication Token",
                "data": None,
                "error": "Unauthorized"
            }, config.HTTP_500_INTERNAL_SERVER_ERROR

        return f(*args, **kwargs)
    return decorated

@app.route("/v1/login", methods=["POST"])
def login():
    try:
        # auth = request.json
        auth = request.authorization
        if not auth:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, config.HTTP_400_BAD_REQUEST
        
        # if auth['password'] == app.config['SECRET_KEY'] and auth['username'] == app.config['USER_NAME']:
        if auth.password == app.config['SECRET_KEY'] and auth.username == app.config['USER_NAME']:
            # if a user is successfullly loggedin return the token
            try:
                token = jwt.encode(
                    {'user':app.config["USER_NAME"]}, 
                    app.config['SECRET_KEY'], 
                    algorithm="HS512"
                )
                return {
                    "message": "Successfully fetched authentication token",
                    "user": app.config['USER_NAME'],
                    "token":token
                }, config.HTTP_200_OK

            except Exception as e:
                return {
                    "error":"Something went wrong",
                    "message":str(e)
                }, config.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "message": "Error fetching authentication token! invalid username or password",
            "data": None,
            "error": "Unauthorized"
        }, config.HTTP_404_NOT_FOUND
    except Exception as e:
        return {
            "error":"Something went wrong",
            "message":str(e),
            "data":None
        }, config.HTTP_500_INTERNAL_SERVER_ERROR




@app.route("/v1/image", methods=["POST"])
@token_required
def detect_image():
    try:
        if request.files.get("image"):
            try:
                image_file = request.files["image"]
                if not image_file:
                    return {
                        "message": "Please provide an image",
                        "data": None,
                        "error": "Bad request"
                    }, config.HTTP_400_BAD_REQUEST

                result = detectObject(image_file)
                result = pd.Series(result).to_json()
                return {
                    "detections":json.loads(result),
                    "messsage":"Successfully processed image"
                }, config.HTTP_200_OK
            except Exception as e:
                return {
                    "error":"Something went wrong",
                    "message":str(e)
                }, config.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "message": "Error processing image! No image parsed",
            "data": None,
        }, config.HTTP_404_NOT_FOUND

    except Exception as e:
        return{
            "error":"Something went wrong",
            "message":str(e),
            "data":None
        }, config.HTTP_500_INTERNAL_SERVER_ERROR



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Car Classifier Api exposing YOLOv4")
    parser.add_argument("-p", "--port", default=8080, type=int, help="port number")
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)