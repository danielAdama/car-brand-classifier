import pytest
import requests
import os
from config import config

@pytest.fixture
def post_response_of_v1_image_endpoint_for_test_jpg():
    url = 'http://localhost:8080/v1/image'
    response = requests.post(
        url, 
        files={'image': open(os.path.join(os.getcwd(),"tests/test1.jpg"), 'rb')},
        headers={'access-token':config.KEYS["TOKEN"]}
    )
    return response