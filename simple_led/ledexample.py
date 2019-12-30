import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledpin = 19

GPIO.setup(ledpin, GPIO.OUT)
GPIO.output(ledpin, GPIO.HIGH)
time.sleep(5)
GPIO.output(ledpin, GPIO.LOW)
GPIO.cleanup()
