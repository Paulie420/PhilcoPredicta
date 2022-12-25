#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import random

buttonPin = 21

directory = "/home/pi/Videos/"

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

def playEpisode():
    episode = random.choice(os.listdir(directory))
    cmd = "nohup omxplayer --aspect-mode stretch "+"'"+directory+episode+"' &"
    print('Killing all omxplayer processes . . .')
    os.system('killall omxplayer.bin')
    os.system(cmd)

try:

#    os.system('clear')
    print('Waiting for button press . . .')
    GPIO.wait_for_edge(buttonPin, GPIO.FALLING)
    print('[x] Recieved button press.')
    print('Playing random video . . .')
    playEpisode()

    #point to location of this file
    os.system('sudo python /home/pi/predicta.py')

except KeyboardInterrupt:
    GPIO.cleanup()
