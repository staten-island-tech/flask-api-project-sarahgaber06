from flask import Flask, render_template
import requests

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    #Get a list of students at Hogwarts
    response = requests.get("https://hp-api.onrender.com/api/characters/students")
    students = response.json()

    #Filter the ones out with missing images
    students_with_images = [student for student in students if student['image']]
    return render_template("index.html, students=student_with_images")

# Route for the student detail page
@app.route("/student/<name>")
def student_detail(name):
    response = requests.get("https://hp-api.onrender.com/api/characters/students")
    students = response.json()
    

