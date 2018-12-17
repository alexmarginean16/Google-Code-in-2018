import time
import datetime
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BCM)
PIR_pin = 11
GPIO.setup(PIR_pin, GPIO.IN)

print("Starting Motion Sensor App (CTRL+C to exit)")
time.sleep(2)
print("Ready!")

try:
	while True:
		i = GPIO.input(PIR_pin)
		if i==1:
			now = datetime.datetime.now()
			now_time = str(now.hour)+":"+str(now.minute)
			
			print("Motion detected! At: ",now_time)
			
			url = "http://192.168.0.103:5000/add/"+now_time
			requests.get(url)
			
			time.sleep(1)
		elif i==0:
			time.sleep(1)
except KeyboardInterrupt:
	print("Quitting...")
	GPIO.cleanup()
