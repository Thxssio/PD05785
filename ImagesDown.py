import requests
from bs4 import BeautifulSoup
import os

def download_images(tag, download_path):
    url = f'https://www.google.com/search?q={tag}&tbm=isch'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img', class_='t0fcAb')

    for i, img_tag in enumerate(img_tags):
        img_url = img_tag['src']
        img_name = os.path.join(download_path, f'{tag}_{i + 1}.jpg')
        img_data = requests.get(img_url).content

        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

# Substitua 'sua_tag' pelo termo que você está procurando e 'C:\\Users\\Thássio\\projetos\\PD05785\\dataset' pelo diretório de destino.
download_images('Isoladores', 'C:\\Users\\Thássio\\projetos\\PD05785\\dataset')
