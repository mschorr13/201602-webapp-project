from os import chdir
from os.path import dirname, realpath
import random

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below


# gets list of list of all classes
def get_data():
    class_list = []
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            class_data = line.split("\t")
            #new_course = Course(*class_data)
            class_list.append(class_data)
        return class_list


# Gets list of list of all fall 2016 classes
def get_fall_2016():
    directory = get_data()  # list of all classes of all years
    fall_2016_list = []
    for n in directory:  # for any individual course,
        if n[0] == '2016' and n[1] == 'fall':
            fall_2016_list.append(n)
    return fall_2016_list


# searches fall 2016 classes for a specific Core requirement and creates new list of courses that satisfy that core
def get_fall_2016_core(core):
    directory = get_fall_2016()
    core_satisfied_list = [] # list of all classes that satisfy specified core requirement
    for n in directory:
        core_possible = n[9].split(";")  # splits multiple core requirements into list of the individual ones
        if core in core_possible:  # if core argument is satisfied by the class, add class to list of classes
            core_satisfied_list.append(n)
    return core_satisfied_list

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
    def __str__(self):
        pass




@app.route('/')
def display_full_courses():
    courses = get_data()
    return render_template('base.html', courses=courses)

@app.route('/CPAF')
def display_random_CPAF():
    courses = get_fall_2016_core('CPAF')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPAS')
def display_random_CPAS():
    courses = get_fall_2016_core('CPAS')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPEU')
def display_random_CPEU():
    courses = get_fall_2016_core('CPEU')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPFA')
def display_random_CPFA():
    courses = get_fall_2016_core('CPFA')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPAP')
def display_random_CPAP():
    courses = get_fall_2016_core('CPAP')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CFAP')
def display_random_CFAP():
    courses = get_fall_2016_core('CFAP')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPGC')
def display_random_CPGC():
    courses = get_fall_2016_core('CPGC')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPIC')
def display_random_CPIC():
    courses = get_fall_2016_core('CPIC')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPLS')
def display_random_CPLS():
    courses = get_fall_2016_core('CPLS')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPLA')
def display_random_CPLA():
    courses = get_fall_2016_core('CPLA')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPMS')
def display_random_CPMS():
    courses = get_fall_2016_core('CPMS')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPEE')
def display_random_CPEE():
    courses = get_fall_2016_core('CPEE')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPRF')
def display_random_CPRF():
    courses = get_fall_2016_core('CPRF')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPUS')
def display_random_CPUS():
    courses = get_fall_2016_core('CPUS')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CPUD')
def display_random_CPUD():
    courses = get_fall_2016_core('CPUD')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

@app.route('/CUSP')
def display_random_CUSP():
    courses = get_fall_2016_core('CUSP')
    course = random.choice(courses)
    return render_template('courses.html', courses=course)

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
    #print(get_fall_2016())
    #print(get_fall_2016_core('CPUD'))
    app.run(debug=True)
