#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(39,GPIO.IN)

GPIO.output(22,GPIO.HIGH)
time.sleep(2)
GPIO.output(22,GPIO.LOW)


	