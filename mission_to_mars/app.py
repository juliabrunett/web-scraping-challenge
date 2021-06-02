# Import dependencies
from flask import Flask, render_template
import scrape_mars
from flask_pymongo import PyMongo

# Initialize app
app = Flask(__name__)

# Connect to the database
mars_db = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# First route
@app.route("/")
def main():

# Scrape function
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()

    return(render_template("index.html", dict= mars_data))