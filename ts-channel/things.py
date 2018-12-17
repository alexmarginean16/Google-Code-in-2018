import urllib2
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import re

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

try:
	while True:
		result = instance.read()
		if result.is_valid():
			data=urllib2.urlopen("https://api.thingspeak.com/update?api_key=PLXNT0HMWT7BLE8O&field1="+str(result.temperature)+"&field2="+str(result.humidity))
			time.sleep(.5)
			print(data.read())
			data.close()
		time.sleep(5)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting...")
	time.sleep(1)
