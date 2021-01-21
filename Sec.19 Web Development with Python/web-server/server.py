#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 256. Building A Flask Server

# https://flask.palletsprojects.com/en/1.1.x/quickstart/

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types 
# https://swapi.dev/   -  Star Wars API server
# http://www.mashup-template.com/templates.html   - Free HTML templates
# https://robohash.org/   - Robot generating API


# We need to run: 
# $ source ./venv/bin/activate
# $ export FLASK_APP=server.py
# $ export FLASK_ENV=development
# $ flask run
 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name =username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def blog():
    return 'Try to type in your browser: "http://127.0.0.1:5000/alex/7" or "http://127.0.0.1:5000/about"'
    

