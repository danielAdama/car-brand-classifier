from imutils import paths
import imutils
import numpy as np
import cv2
import os
import sys
sys.path.append('/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/car-brand-classifier')
from detector.car import CarDetector

def test_car():
    cd = CarDetector(weight='yolov4-tiny.weights', cfg='yolov4-tiny.cfg')
    image = os.path.join(os.getcwd(),"tests/pexels-nordic-overdrive-627719.jpg")
    frame = cv2.imread(image)
    frame = imutils.resize(frame, 900)
    (height, width) = frame.shape[:2]
    frame = cv2.resize(frame, (width, height))
    boxes = cd.vehicle_detected(frame)
    # Actual representation
    actual = np.array(boxes[0], dtype='int32')
    expected = np.array([168, 176, 486, 172], dtype='int32')
    assert len(actual) == 4
    assert np.array_equal(actual, expected) is True