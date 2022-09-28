import requests
from bs4 import BeautifulSoup
import os

# from config import config


# urls, basePath, brand_names
def scrape_images(basePath):
    
    """Function to download image data from 'https://www.izmostock.com/'
    """
    imagepath = []

    u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    }

    num_to_scrape = 3
    car_info = str(input('Enter Car brand format as in square bracket: [Year Brand Model]: ')).lower()
    # 2015 Toyota Camry
    year, brand, model = int(car_info.split()[0]), car_info.split()[1], car_info.split()[2]
    url = f"https://cars.usnews.com/cars-trucks/{brand}/{model}/{year}/photos-exterior"

    page = requests.get(url, headers=u_agnt)
    soup = BeautifulSoup(page.text, 'html.parser')
    imagelinks = [item['src'] for item in soup.find_all('img')]
    for idx, imagelink in enumerate(imagelinks):
        if imagelink.split()[0].split('.')[-1] == 'jpg':
            # Download only 50 images
            if idx == num_to_scrape:
                break
            # response = requests.get(imagelink)
            brandPath = os.path.join(basePath,f'{brand}_{model}_{year}')
            if not os.path.exists(brandPath):
                os.mkdir(brandPath)
    #         imagename = os.path.join(basePath,brand,str(idx+1)+'.jpg')
    #         # Store images
    #         with open(imagename, 'wb') as file:
    #             file.write(response.content)
    #     print(f"Images for {brand} cars downloaded successfully")
    # print("Done! Downloading")

if __name__ == '__main__':
    
    # BRAND_NAMEs = ["Audi", "BMW", "Toyota", "Mercedes", "Lexus"]
    # CAR_URLs = [
    #     "https://archive.izmostock.com/search?I_DSC=Audi+A6&I_DSC_AND=t&_ACT=search",
    #     "https://archive.izmostock.com/search?I_DSC=bmw&I_DSC_AND=t&_ACT=search",
    #     "https://archive.izmostock.com/search?I_DSC=toyota&I_DSC_AND=t&_ACT=search",
    #     "https://archive.izmostock.com/search?I_DSC=mercedes&I_DSC_AND=t&_ACT=search",
    #     "https://archive.izmostock.com/search?I_DSC=lexus&I_DSC_AND=t&_ACT=search"
    # ]

    BASEPATH = r"C:\Users\DELL\Desktop\programming\computerVision\dataset\car_brand\new_custome"

    scrape_images(basePath=BASEPATH)