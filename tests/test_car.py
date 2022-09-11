from imutils import paths
import imutils
import numpy as np
import cv2
import os
from detector.car import CarDetector

def test_car():
    cd = CarDetector(weight='yolov4.weights', cfg='yolov4.cfg')
    image = os.path.join(os.getcwd(),"tests/pexels-svh-2684219.jpg")
    frame = cv2.imread(image)
    frame = imutils.resize(frame, 900)
    (height, width) = frame.shape[:2]
    frame = cv2.resize(frame, (width, height))
    boxes = cd.vehicle_detected(frame)
    actual = np.array(boxes[0], dtype='int32')
    expected = np.array([115, 213, 718, 223], dtype='int32')
    # expected = [115, 213, 718, 223]
    assert len(actual) == 4
    assert np.array_equal(actual, expected) is True