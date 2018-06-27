#!/usr/bin/python
# banco.py 

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
								
								
