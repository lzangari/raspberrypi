import RPi.GPIO as GPIO
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--d", type=int, default=5)
args = parser.parse_args()


GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
led = 19
distance_response = args.d

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, GPIO.LOW)

while True:
	
	GPIO.output(TRIG, True)
	time.sleep(0.000000001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO) == False:
		start = time.time()
	
	while GPIO.input(ECHO) == True:
		end = time.time()
	
	sig_time = end-start
	distance = sig_time / 0.000058

	print('Distance: {} cm'.format(distance))
	
	if distance > distance_response:
		GPIO.output(led, GPIO.HIGH)
	else:
		GPIO.output(led, GPIO.LOW)

GPIO.cleanup()
