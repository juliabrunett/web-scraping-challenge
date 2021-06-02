# Import dependencies
from flask import Flask, render_template
import scrape_mars

# Initialize app
app = Flask(__name__)

# First route
@app.route("/")
def main():