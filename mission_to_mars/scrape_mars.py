# Import dependenices
from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Initialize app
app = Flask(__name__)

# Create executable path to open a browser for the scraping: using WebDriver Manager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Scrape function
@app.route("/scrape")
def scrape():
    #1
    # Define the url 
    url = 'https://redplanetscience.com/'  

    # Visit the website using splinter
    browser.visit(url)

    # Iterate once to find the container, and then the latest news title and paragraph
    for x in range(1):
        html = browser.html
        soup = bs(html, 'html.parser')
    
        # Define the container
        container = soup.find('section', class_='image_and_description_container')
    
        # Grab the title and paragraph text
        news_title = container.find('div', class_='content_title').text
        news_p = container.find('div', class_='article_teaser_body').text
    
        print(news_title)
        print(news_p)

    #2
    # Url for jpl images
    url = 'https://spaceimages-mars.com/'

    # Visit the website
    browser.visit(url) 
    
    # Iterate once to find the container, and then click the button to see the full image
    # find the url for the latest featured image
    for x in range(1):
        html = browser.html
        soup = bs(html, 'html.parser')
    
        # Define the container
        container = soup.find('div', class_='floating_text_area')
    
        # Click on the full image button to get the full image
        browser.links.find_by_partial_text('FULL IMAGE').click()
    
        # Define the box
        box = container.find('a', class_='showimg fancybox-thumbs')
    
        # Grab the featured image url
        featured_image_url = box['href']
        featured_image_url = url + featured_image_url
    
        print(featured_image_url)
    
    #3
    # Url for table facts
    url = 'https://galaxyfacts-mars.com/'

    # Find table data and load into pandas
    tables = pd.read_html(url)
    print(tables)

    # Create a dataframe from the first table
    mars_earth_df = tables[0]
    mars_earth_df = mars_earth_df.rename(columns = mars_earth_df.iloc[0])
    mars_earth_df = mars_earth_df.set_index("Mars - Earth Comparison")
    mars_earth_df = mars_earth_df.iloc[1:]
    print(mars_earth_df)

    #4
    # Define the url
    url = 'https://marshemispheres.com/'

    # Access the html and parse through it
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Create a hemispheres list
    hemisphere_image_urls = []
    
    # Get the 4 descriptions for the website - h3
    descriptions = soup.find_all('h3', limit=4)

    # Visit the url
    browser.visit(url)

    # Iterate through the descriptions
    for title in descriptions:
            
        # Click on the description to get the full image
        browser.links.find_by_partial_text(title.text).click()
            
        # Create a new html browser query for the new page
        html = browser.html
        soup = bs(html, 'html.parser')
            
        # Find the downloads box
        downloads = soup.find('div', class_='downloads')
            
        # Find the downloads list
        img_list = downloads.find('li')
            
        # Get the first list object's href
        img_url = img_list.a['href']
    
        # Create the full url for the image
        img_url = url + img_url
    
        # Create a dictionary of the values
        dictionary = {
            "title": title.text,
            "img_url": img_url
            }
    
        # Append the dictionary to the hemispheres list
        hemisphere_image_urls.append(dictionary) 

        # Navigate back to the main page
        browser.back()

        print(hemisphere_image_urls)
        
if __name__ == "main":
    app.run(debug=True)