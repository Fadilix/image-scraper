# Image Scraper
The utility of this program is to automate the process of downloading images from a specified website
(Is really helpfull when you are cloning websites and you need assets from a website)

## Prerequisites
Before using this script, make sure you have the following Python libraries installed:
- requests: To send HTTP requests to the website
- BeautifulSoup: To parse the HTML content of the web page
- os: To create directories for downloaded images
- urllib.parse.urljoin: To unsure that image URLs are absolute

```
pip install requests beautifulsoup4
```

## Usage

- Open the script (web_image_scraper.py) in a Python code editor.
- Replace the website_url variable with the URL of the website you want to scrape.
- Replace the save_directory variable with the directory where you want to save the downloaded images. The script will create this directory if it doesn't already exist.
- Run the script:
```
python web_image_scraper.py
```
The script will connect to the specified website, find all image tags (<img>) in the HTML content, and download the images to the specified directory.

## Example

```
if __name__ == "__main__":
    website_url = "https://example.com"  # Replace with the URL of the website you want to scrape
    save_directory = "downloaded_images"  # Replace with the directory where you want to save the images
    scrape_images_from_website(website_url, save_directory)
```

## Screenshots
### Targeted site
![image](https://github.com/Fadilix/image-scraper/assets/121851593/bd502a47-9be6-4aad-a5a3-1a099f09bb84)

### Process
![image](https://github.com/Fadilix/image-scraper/assets/121851593/8b573806-7d7b-4cc9-9142-d57517fcbd20)

### Result
![image](https://github.com/Fadilix/image-scraper/assets/121851593/b0ca5d25-da25-4d4c-a0b4-c2e1eb50752e)





