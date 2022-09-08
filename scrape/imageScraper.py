import requests
from bs4 import BeautifulSoup
import os
from config import config



def scrape_images(urls, basePath, brand_names):
    
    """Function to download image data from 'https://www.izmostock.com/'
    """
    imagepath = []
    for url, brand in zip(urls, brand_names):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        imagelinks = [item['src'] for item in soup.find_all('img')]
        for idx, imagelink in enumerate(imagelinks):
            # Download only 50 images
            if idx == 50:
                break
            response = requests.get(imagelink)
            brandPath = os.path.join(basePath,f'{brand}')
            if not os.path.exists(brandPath):
                os.mkdir(brandPath)
            imagename = os.path.join(basePath,brand,str(idx+1)+'.jpg')
            # Store images
            with open(imagename, 'wb') as file:
                file.write(response.content)
        print(f"Images for {brand} cars downloaded successfully")
    print("Done! Downloading")

if __name__ == '__main__':

    BASEPATH = "/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/dataset/car_brand/custome_data"
    BRAND_NAMEs = ["Audi", "BMW", "Toyota", "Mercedes", "Lexus"]
    CAR_URLs = [
        "https://archive.izmostock.com/search?I_DSC=Audi+A6&I_DSC_AND=t&_ACT=search",
        "https://archive.izmostock.com/search?I_DSC=bmw&I_DSC_AND=t&_ACT=search",
        "https://archive.izmostock.com/search?I_DSC=toyota&I_DSC_AND=t&_ACT=search",
        "https://archive.izmostock.com/search?I_DSC=mercedes&I_DSC_AND=t&_ACT=search",
        "https://archive.izmostock.com/search?I_DSC=lexus&I_DSC_AND=t&_ACT=search"
    ]

    scrape_images(CAR_URLs, config.BASEPATH, config.BRAND_NAMES)