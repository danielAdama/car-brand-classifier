import os 
import cv2

WEIGHTS = 'dnn_model/yolov4.weights'
EXAMPLE_IMGS = 'examples'
CFG = 'dnn_model/yolov4.cfg'
DATAPATH = "/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/car_brand/custome_data"
# BASEPATH = "/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/car_brand/custome_new"
BRAND_NAMES = ["Audi", "BMW", "Toyota", "Mercedes", "Lexus", "Honda"]
NUM_IMAGES_TO_SCRPE = 80
FONT = cv2.FONT_HERSHEY_COMPLEX