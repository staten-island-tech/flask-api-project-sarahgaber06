from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to get students with real image URLs
def get_students_with_images():
    response = requests.get("https://hp-api.onrender.com/api/characters/students")
    students = response.json()
    return [s for s in students if s.get("image") and s["image"].strip()]

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Students page
@app.route("/students")
def show_students():
    students = get_students_with_images()
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
