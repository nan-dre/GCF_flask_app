#!/usr/bin/python
from flask import Flask, render_template, request
import requests
import re
import os
app = Flask(__name__)

SEQUENCE_LENGTH = 8
DIVERSITY = 0.5
QUANTITY = 125

def convert(input):
    # Converts unicode to string
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, str):
        return input.encode('utf-8')
    else:
        return input

@app.route("/")
def target():
    return render_template('index.html')

@app.route("/generate", methods=['GET', 'POST'])
def processing():
    url = os.getenv('URL')
    data = request.form['prompt']
    data = data.lower()
    data = '{"seed": "%s", "sequence_length": "%d", "diversity": "%f", "quantity": "%d"}' % (data, SEQUENCE_LENGTH, DIVERSITY, QUANTITY)
    print(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    text = response.text
    text = re.sub(r'\n', '<br>', text)
    return text

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
