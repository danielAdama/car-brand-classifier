import pytest
import requests
import os


def test_api_post_image_endpoint(post_response_of_v1_image_endpoint_for_test_jpg):
    assert post_response_of_v1_image_endpoint_for_test_jpg.status_code == 200
