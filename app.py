from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
API_URL = "https://hp-api.onrender.com/api/characters/students"

def fetch_students():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return [s for s in response.json() if s.get("image") and s["image"].strip()]
    except requests.RequestException:
        return []

def get_students_by_house(house):
    return [s for s in fetch_students() if s.get("house", "").lower() == house.lower()]

def get_student_by_name(name):
    for student in fetch_students():
        if student.get("name", "").lower() == name.lower():
            return student
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def show_students():
    house_filter = request.args.get("house")
    search_name = request.args.get("name")

    students = fetch_students()
    if house_filter:
        students = [s for s in students if s.get("house", "").lower() == house_filter.lower()]
    if search_name:
        students = [s for s in students if search_name.lower() in s.get("name", "").lower()]

    return render_template("students.html", students=students)

@app.route("/student/<name>")
def student_profile(name):
    student = get_student_by_name(name.replace("%20", " "))
    if student:
        return render_template("student_detail.html", student=student)
    return "Student not found", 404

if __name__ == "__main__":
    app.run(debug=True)
