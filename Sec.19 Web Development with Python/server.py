#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 256. Building A Flask Server

# https://flask.palletsprojects.com/en/1.1.x/quickstart/

# We need to run:
# $ source ./venv/bin/activate
# $ export FLASK_APP=server.py
# $ export FLASK_ENV=development
# $ flask run
 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Alex2!'
