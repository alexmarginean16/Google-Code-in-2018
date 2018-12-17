import urllib2
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

while True:
	data = urllib2.urlopen("http://192.168.0.105:5000")
	for line in data:
		if line < '20':
			GPIO.output(4, True)
		if line == '100':
			GPIO.output(4, False)
	time.sleep(1)