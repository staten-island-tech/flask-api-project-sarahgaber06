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
    from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students')
def students():
    # Example list of students to pass to the template
    students_data = [
        {
            'name': 'Harry Potter',
            'house': 'Gryffindor',
            'image': 'harry.jpg',
            'species': 'Human',
            'gender': 'Male',
            'dateOfBirth': '31-07-1980',
            'yearOfBirth': 1980,
            'ancestry': 'Half-blood',
            'eyeColour': 'Green',
            'hairColour': 'Black',
            'wand': {'wood': 'Holly', 'core': 'Phoenix feather', 'length': '11'},
            'patronus': 'Stag',
            'hogwartsStudent': True,
            'hogwartsStaff': False,
            'actor': 'Daniel Radcliffe',
            'alternate_names': [],
            'alive': True
        },
        # Add more students as needed
    ]

    return render_template('students.html', students=students_data)
