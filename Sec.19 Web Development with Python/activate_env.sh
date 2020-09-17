#!/bin/bash

source ./venv/bin/activate && echo Virtual Environment is activated

export FLASK_APP=server.py

flask run&
