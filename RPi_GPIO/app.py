import RPi.GPIO as GPIO
import time
import dht11
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buttonPin = 24
ledPin = 21
LDRPin = 3
PIRPin = 11

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(LDRPin, GPIO.IN)
GPIO.setup(PIRPin, GPIO.IN)

#Setting LED to no light
GPIO.output(ledPin, GPIO.LOW)

instance = dht11.DHT11(pin=17)

try:
	print("GPIO task for Google Code-In App (CTRL+C to quit)")
	print("Press and hold the button until the LED lights up")
	time.sleep(1)
	print("Ready!")

	while True:
		#Getting button state and the humidity/temperature result
		result = instance.read()
		button_state = GPIO.input(buttonPin)
		if button_state == False and result.is_valid():
			print("Displaying information for "+str(datetime.datetime.now()))
			time.sleep(1)
			GPIO.output(ledPin,GPIO.HIGH)
			#DHT11 INFO
			print("Temperature: %d C" % result.temperature)
			time.sleep(1)
			print("Humidity: %d %%" % result.humidity)
			time.sleep(1)
			#LDR INFO
			dark = GPIO.input(LDRPin)
			if dark == 1:
				print("Dark")
			else:
				print("Light")
			time.sleep(1)
			#PIR INFO
			i = GPIO.input(PIRPin)
			if i == 0:
				print("No motion")
			elif i == 1:
				print("Motion detected!")
			time.sleep(1)
			GPIO.output(ledPin,GPIO.LOW)
			print("Done")
except KeyboardInterrupt:
	print("Quitting...")
	GPIO.cleanup()
	time.sleep(1)
	print("Done!")
