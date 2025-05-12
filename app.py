from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    #Ask the Disney API for the first 15 Disney Characters
    response = requests.get("")