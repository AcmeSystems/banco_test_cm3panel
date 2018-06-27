#!/usr/bin/python

# monitor.py 
# In Circuit Programming utility for FOX Board and Netus G20  

# Versione per banco basato su CM3-Panel

import time
import sys
import getopt
import string 
import time
import sys
import getopt
import string 
import datetime
import RPi.GPIO as GPIO
import os

# GPIO usati per inviare comandi
#power_on=31
#chip_enable=26
#switch_up=27
#switch_down=28
#switch_toggle=29

color_blue = "\x1B[34;40m"
color_white = "\x1B[37;40m"

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False) 
#GPIO.setup(power_on, GPIO.OUT)
#GPIO.setup(chip_enable, GPIO.OUT)
#GPIO.setup(switch_up, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(switch_down, GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.setup(switch_toggle, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#GPIO.output(chip_enable,0)
#GPIO.output(power_on,0)

print "Banco test CM3-Panel"

os.system("clear <> /dev/console >&0 2>&1")
os.system("echo 'Test backlight' <> /dev/console >&0 2>&1")
time.sleep(1)
os.system("/home/pi/banco_test_cm3panel/backlight.py <> /dev/console >&0 2>&1")
os.system("echo 'Fine test backlight' <> /dev/console >&0 2>&1")
os.system("echo '------------------------------------' <> /dev/console >&0 2>&1")
os.system("echo 'Test touch: tocca lo schermo' <> /dev/console >&0 2>&1 &")
time.sleep(1)
os.system("/home/pi/banco_test_cm3panel/touch.py <> /dev/console >&0 2>&1 &")
time.sleep(3)
os.system("pkill touch.py")
os.system("echo 'Fine test touch' <> /dev/console >&0 2>&1")
os.system("echo '------------------------------------' <> /dev/console >&0 2>&1")
os.system("echo 'Test camera:' <> /dev/console >&0 2>&1")
time.sleep(1)
os.system("/home/pi/banco_test_cm3panel/camera.py <> /dev/console >&0 2>&1")
os.system("echo 'Fine test touch' <> /dev/console >&0 2>&1")
os.system("echo '------------------------------------' <> /dev/console >&0 2>&1")
os.system("echo 'Test GPIO:' <> /dev/console >&0 2>&1")
time.sleep(1)
os.system("/home/pi/banco_test_cm3panel/gpio.py <> /dev/console >&0 2>&1")
os.system("echo 'Fine test GPIO' <> /dev/console >&0 2>&1")

os.system("echo 'FINE TEST' <> /dev/console >&0 2>&1")

while True:
	time.sleep(1)
								
								