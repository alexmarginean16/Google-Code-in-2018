
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import time
app = Flask(__name__)

# CONFIG INFO FOR YOUR OWN DATABASE
#app.config["MONGO_DBNAME"] = ''
#app.config["MONGO_URI"] = ""

mongo = PyMongo(app)

@app.route('/')
def hello():
    return "Welcome :)"

@app.route('/add/<time>', methods=['GET', 'POST'])
def add(time):
	if request.method == 'GET':
		times = mongo.db.times
		times.insert({'Action' : 'Motion Detected!', 'time' : time})
		return 'Added motion'

if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.run(debug=True, host='192.168.0.103', port=5000)
