import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to create a directory for downloaded images
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download an image
def download_image(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(directory, os.path.basename(url)), 'wb') as f:
            f.write(response.content)
            print(f"Downloaded: {os.path.basename(url)}")
    else:
        print(f"Failed to download: {url}")

# Function to scrape and download images from a website
def scrape_images_from_website(url, save_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            create_directory(save_directory)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all image tags
            img_tags = soup.find_all('img')
            
            for img in img_tags:
                img_url = img.get('src')
                if img_url:
                    img_url = urljoin(url, img_url)  # Make sure the URL is absolute
                    download_image(img_url, save_directory)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    website_url = "" # Replace with the URL of the website you want to scrape
    save_directory = "downloaded_images"  # Replace with the directory where you want to save the images
    scrape_images_from_website(website_url, save_directory)
