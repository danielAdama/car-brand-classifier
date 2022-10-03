import os 
import cv2

EXAMPLE_IMGS = r'C:/Users/Dell/Desktop/programming/computerVision/car-brand-classifier/examples'
VIDEO = 'Traffic.mp4'
BASEPATH = r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier'
# DATAPATH = r"C:/Users/Dell/Desktop/programming/computerVision/dataset/car_brand/custome_data"
# BASEPATH = "/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/car_brand/custome_new"
BRAND_NAMES = ["Audi", "BMW", "Toyota", "Mercedes", "Lexus", "Honda"]
NUM_IMAGES_TO_SCRPE = 80
FONT = cv2.FONT_HERSHEY_COMPLEX