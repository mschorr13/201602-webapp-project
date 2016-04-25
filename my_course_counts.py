from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below
def get_data():
    class_list = []
    num = 0
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            class_data = line.split("\t")
            new_course = Course(*class_data)
            class_list.append(new_course)
        return class_list

class Course:
    def __init__(self, year, season, department, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.title = title
        self.units = units
        self.instructors = instructors
        self.meetings = meetings
        self.core = core
        self.seats = seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted


@app.route('/')
def display_full_courses():
    courses = get_data()
    return render_template('base.html', courses=courses)

# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    #print(get_data())
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)
