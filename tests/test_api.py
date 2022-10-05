import pytest
from flask import Flask, request, jsonify
from api.api import detect

def test_post_route_success():
    app = Flask(__name__)
    client = app.test_client()
    # Testing the '/v1/image' route
    url = 'http://localhost:8080/v1/image'

    response = client.post(url, files={'image': open('test.jpg', 'rb')})


