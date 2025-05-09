from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # We ask the Cat API for the first 15 Cat facts.
    response = requests.get("curl https://meowfacts.herokuapp.com/?count=15")
    data = response.json()
    cat_facts = data['results']
    
#We will create a list to show facts for each cat
cat_facts = []
    
for cat_fact in cat_facts:
        url = cat_facts['url']
        parts = url.strip("/").split("/")
        id = parts[-1] 

