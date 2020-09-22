#!/bin/bash

source ./venv/bin/activate && echo Virtual Environment is activated

export FLASK_APP=server.py
export FLASK_ENV=development

flask run
