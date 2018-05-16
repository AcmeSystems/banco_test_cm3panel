import RPi.GPIO as GPIO
import time
import sys
import getopt
import string 
import datetime
import select
import sys
import os
import termios
import tty
from evdev import InputDevice,ecodes


#http://www.termsys.demon.co.uk/vtansi.htm
color_white = "\x1B[37;40m"
color_red = "\x1B[31;40m"
clear_screen = "\x1B[2J"
cursor_home = "\x1B[H"
white_blue = "\x1B[37;44m" 


x=0
y=0
device = InputDevice('/dev/input/event0')

for event in device.read_loop():
	if event.type==ecodes.EV_ABS:
		print event.code,event
		if event.code==53:
			x=event.value
		if event.code==54:
			y=event.value			
		print x,y	
						


	
