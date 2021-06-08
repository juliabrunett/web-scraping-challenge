# web-scraping-challenge
***Web Scraping Homework:*** This assignment used Beautiful Soup, Splinter, and ChromeDriverManager to scrape text, images, and tables from various websites with Mars information. The scraped data was then rendered using Flask and PyMongo to store the information in a MongoDB database and push it through an html template. By running the [app.py](/mission-to-mars) and clicking the "Scrape for the Latest Mars Data" button, you can discover the latest mars news from [Red Planet Science](https://redplanetscience.com/), see a featured mars image from [JPL](https://spaceimages-mars.com), discover mars facts from [Galaxy Facts](https://galaxyfacts-mars.com), and view each of mars hemispheres from [Mars Hemispheres](https://marshemispheres.com/).

**mission-to-mars folder:**
- ***static:*** styles.css (CSS for html format)
- ***templates:*** index.html (HTML template for main page)
- *app.py:* main app using Flask to render HTML
- *mission_to_mars.ipynb:* jupyter notebook with web-scraping code
- *scrape_mars.py:* python file with web-scraping code from the jupyter notebook
