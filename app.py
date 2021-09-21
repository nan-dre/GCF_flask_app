#!/usr/bin/python
from flask import Flask, render_template, request
import time
import urllib.parse
import requests
app = Flask(__name__)

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
	url = 'https://europe-central2-hallowed-pager-326510.cloudfunctions.net/lstm_character_generation'
	data = request.form['prompt']
	data = '{"prompt": "'+ data + '"}'
	headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=data, headers=headers)
	text = response.text 
	return render_template('generate.html', passed_data = text)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug=True)
