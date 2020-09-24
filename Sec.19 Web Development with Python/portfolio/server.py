#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 256. Building A Flask Server

# https://flask.palletsprojects.com/en/1.1.x/quickstart/

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types 
# https://swapi.dev/   -  Star Wars API server
# http://www.mashup-template.com/templates.html   - Free HTML templates
# https://html5up.net/   - Free HTML templates
# https://robohash.org/   - Robot generating API


# We need to run:
# $ source ./venv/bin/activate
# $ export FLASK_APP=server.py
# $ export FLASK_ENV=development
# $ flask run
 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home():
    print(render_template('index.html'))
    return render_template('index.html')

@app.route('/index.html')
def index():
    print(render_template('index.html'))
    return render_template('index.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    print(render_template('about.html'))
    return render_template('about.html')
 
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
