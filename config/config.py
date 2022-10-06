import os 
import cv2



HTTP_200_OK = 200
HTTP_400_BAD_REQUEST = 400
HTTP_403_UNAUTHORIZED = 403
HTTP_404_NOT_FOUND = 404
HTTP_500_INTERNAL_SERVER_ERROR = 500

KEYS = {
    "USER_NAME":"admin",
    "SECRET_KEY":"summer_123.",
    "TOKEN":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.2cKh3mFLAcdiykvlNaNGNatAF3TXmAcBHSYaiEeb1dLgwxb45DaRZqFlB8gdhsQ8i93oiDOgSNMJxuDE6dDigA"
}
EXAMPLE_IMGS = r'C:/Users/Dell/Desktop/programming/computerVision/car-brand-classifier/examples'
VIDEO = 'Traffic.mp4'
BASEPATH = r'C:\Users\DELL\Desktop\programming\computerVision\car-brand-classifier'
# DATAPATH = r"C:/Users/Dell/Desktop/programming/computerVision/dataset/car_brand/custome_data"
# BASEPATH = "/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/car_brand/custome_new"
BRAND_NAMES = ["Audi", "BMW", "Toyota", "Mercedes", "Lexus", "Honda"]
NUM_IMAGES_TO_SCRPE = 80
FONT = cv2.FONT_HERSHEY_COMPLEX