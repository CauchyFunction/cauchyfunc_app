from app import app
from flask import jsonify, request

@app.route('/')
def index():
	return "Hello, World!";

@app.route('/data')
def data():
	data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
	return jsonify(data)
