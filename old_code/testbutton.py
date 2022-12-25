# https://gist.github.com/Vontux/db61a8ac7d25cf39d076d3f697161761
# TTP223 Capacitive Touch Switch, github python code & youtube video:
# https://www.youtube.com/watch?v=hOvfvumFIpg

#!/usr/bin/env python
#tweaked a script from an adafruit tutorial
#https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi?view=all
import os
from time import sleep
import random
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
answers = [
    "Oh my...",
    "keep touching",
    "bad touch...I like it",
    "oh boy...thats the stuff",
    "hey there baby...keep it up",
    "Yep...I enjoy this touching greatly human",
    "You complete my circuit...",
    "The mitochondria is the powerhouse of the cell",
]
 
while True:
    if (GPIO.input(21) == True):
       print random.choice(answers) 
    sleep(0.1);
