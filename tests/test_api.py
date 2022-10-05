import pytest
import requests
import os


def test_api_post_image_endpoint():
    url = 'http://localhost:8080/v1/image'
    response = requests.post(url, files={'image': open(os.path.join(os.getcwd(),"tests/test.jpg"), 'rb')})
    # response.
    assert response.status_code == 200
