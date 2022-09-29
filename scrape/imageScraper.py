import requests
from bs4 import BeautifulSoup
import os

# from config import config


def scrape_images(basePath):
    
    """Function to download image data from 'https://cars.usnews.com/cars-trucks'
    """
    u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }

    num_to_scrape = 500
    list_parts_not_allowed = ["doorhandle", "engine", "grille", "headlight", "mirror", "taillight", "trunk", "wheelcap"]

    car_info = str(input('Enter Car brand format as in square bracket: [Year Brand Model]: ')).lower()
    # 2015 Toyota Camry
    year, brand, model = int(car_info.split()[0]), car_info.split()[1], car_info.split()[2]
    url = f"https://cars.usnews.com/cars-trucks/{brand}/{model}/{year}/photos-exterior"

    page = requests.get(url, headers=u_agnt)
    soup = BeautifulSoup(page.text, 'html.parser')
    imagelinks = [item['src'] for item in soup.find_all('img')]
    for idx, imagelink in enumerate(imagelinks):
        if imagelink.split('.')[-1] == 'jpg':
            # Number of images allowed to download
            if idx == num_to_scrape:
                break
            response = requests.get(imagelink, headers=u_agnt)
            brandPath = os.path.join(basePath,f'{brand}_{model}_{year}')
            # print(f"Folder Created: {brandPath} for {brand}")
            if not os.path.exists(brandPath):
                os.mkdir(brandPath)
            jpg_car = imagelink.split('/')[-1].lower()
            if jpg_car.split('_')[-1].split('.')[0] not in list_parts_not_allowed:
                imagename = os.path.join(brandPath,jpg_car)
                # Store images
                with open(imagename, 'wb') as file:
                    file.write(response.content)
                print(f"Images {jpg_car} for '{brand.capitalize()} {model.capitalize()} {year}' cars downloaded successfully")
    print("Done! Downloading")

if __name__ == '__main__':
    
    BASEPATH = r"C:\Users\DELL\Desktop\programming\computerVision\dataset\car_brand\new_custome"
    scrape_images(basePath=BASEPATH)