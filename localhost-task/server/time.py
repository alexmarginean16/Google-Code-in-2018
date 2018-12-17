from flask import Flask
import psutil
app = Flask(__name__)


@app.route('/')
def hello():
	battery = psutil.sensors_battery()
	percent = battery.percent
	return str(percent)

if __name__ == '__main__':
	app.debug = True
	app.run(host='192.168.0.105', port=5000)