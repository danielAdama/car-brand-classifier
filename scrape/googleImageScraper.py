import os
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append('/home/daniel/Desktop/programming/pythondatascience/datascience/computerVision/car-brand-classifier')
from config import config

Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main():
    ch = 'Y'

    while (ch == 'Y' or ch == 'y'):
        data = input('Enter your search keyword: ')
        num_images = int(input('Enter the number of images you want: '))
        scrape_car_images(num_images, data)
        ch = input("\n Press 'Y' to continue or 'N' to exit: ")
        if ch == 'N' or ch == 'n':
            break

def scrape_car_images(num_images, data):

    """Function to download image data from 'https://www.google.com/'
    """
    print('\nSearching Images....')
    search_url = Google_Image + 'q=' + data
    response = requests.get(search_url, headers=u_agnt)
    b_soup = BeautifulSoup(response.text, 'html.parser')
    results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    count = 0
    imagelinks = []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if(count >= num_images):
                break
        except KeyError:
            continue

    print(f'Found {len(imagelinks)} images for {data}')
    print('Start downloading...')
    
    for idx, imagelink in enumerate(imagelinks):
        if idx == num_images:
            break
        response = requests.get(imagelink)
        dataPath = os.path.join(config.BASEPATH,f'{data}')
        if not os.path.exists(dataPath):
            os.mkdir(dataPath)
        imagename = os.path.join(config.BASEPATH,data,str(idx+1)+"n"+'.jpg')
        with open(imagename, 'wb') as file:
            file.write(response.content)
    print(f"Images for '{data}' cars downloaded successfully")

# if __name__ == '__main__':
#     main()