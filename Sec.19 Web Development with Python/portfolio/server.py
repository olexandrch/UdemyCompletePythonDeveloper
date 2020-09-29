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
 
import os
import datetime
import csv
from flask import Flask, render_template, request, send_from_directory, redirect

app = Flask(__name__)

@app.route('/')
def my_home():
    print(render_template('index.html'))
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


# https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'assets'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def write_to_file(data):
    """Write message to the database.txt"""
    with open('database.txt', mode='a') as database:
        date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'{date},   {email},   {subject},   {message}\n')

def write_to_csv(data):
    """Write message to the database.csv"""
    with open('database.csv', mode='a') as database:
        date = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        message_writer = csv.writer(database, delimiter=',',
                 quotechar='"', quoting=csv.QUOTE_NONE) 
        message_writer.writerow([date, email, subject, message])
