thonimport requests
from bs4 import BeautifulSoup
import os

def extract_image_urls(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve URL: {url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = [img['src'] for img in soup.find_all('img', src=True)]
    return image_urls

def download_image(url, folder_path):
    img_data = requests.get(url).content
    img_name = os.path.basename(url)
    img_path = os.path.join(folder_path, img_name)
    
    with open(img_path, 'wb') as f:
        f.write(img_data)

def save_images_from_url(url, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    image_urls = extract_image_urls(url)
    for img_url in image_urls:
        download_image(img_url, save_folder)
    print(f"Downloaded {len(image_urls)} images to {save_folder}")