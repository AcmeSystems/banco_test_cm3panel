import RPi.GPIO as GPIO
import time
import sys
import getopt
import string 
import datetime
import select
import sys
import os

def separator():
	print " "	
	print "=============================================================================="
	print " "	

color_white = "\x1B[37;40m"
color_red = "\x1B[31;40m"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test = [ 
	[42,35],
	[43,36],
	[44,37],
	[45,38],

	[34,23],
	[33,24],
	[32,25],
	[31,26],
	[30,27],
	[29,28],
]

print "***********************"
print " Test CM3-Panel        "
print "***********************"

for gpios in test:
	error_counter=0
	print "Test %d -> %d" % (gpios[0],gpios[1])

	GPIO.setup(gpios[0],GPIO.OUT)
	GPIO.setup(gpios[1],GPIO.IN)

	GPIO.output(gpios[0],GPIO.HIGH)
	if GPIO.input(gpios[1])<>1:
		print color_red + "  Error hi to low" + color_white
		error_counter = error_counter + 1

	GPIO.output(gpios[0],GPIO.LOW)
	if GPIO.input(gpios[1])<>0:
		print color_red + "  Error low to hi" + color_white
		error_counter = error_counter + 1

	print "Test %d -> %d" % (gpios[1],gpios[0])

	GPIO.setup(gpios[0],GPIO.IN)
	GPIO.setup(gpios[1],GPIO.OUT)

	GPIO.output(gpios[1],GPIO.HIGH)
	if GPIO.input(gpios[0])<>1:
		print color_red + "  Error hi to low" + color_white
		error_counter = error_counter + 1

	GPIO.output(gpios[1],GPIO.LOW)
	if GPIO.input(gpios[0])<>0:
		print color_red + "  Error low to hi" + color_white
		error_counter = error_counter + 1





	