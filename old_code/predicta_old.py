#!/usr/bin/python

import time
import os
import random
from gpiozero import Button
from signal import pause
from contextlib import contextmanager
import sys

buttonPin = 21
directory = "/home/pi/Videos/"

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def playEpisode():
    with suppress_stdout():
        episode = random.choice(os.listdir(directory))
#Must figure out; do we want --aspect-mode stretch or NOT. on Predicta...
        cmd = "nohup omxplayer --aspect-mode stretch "+"'"+directory+episode+"' &"
#        cmd = "nohup omxplayer "+"'"+directory+episode+"' &"
        os.system('sudo killall omxplayer.bin')
        os.system('sudo killall omxplayer')
        os.system(cmd)
#       the following DOESNT work to keep playing MORE videos after one ends...
#       currently, it waits for another buttonpress. i want more to play if no
#       buttonpress. :/
#       playEpisode()

#Below does play random videos one after another, from a LIST - but doesnt
#allow for button presses; omxplayer continues.... grrrrr. 5/30/22
#def playEpisode():
#    videoList = os.listdir(directory)
#    random.shuffle(videoList)
#    for video in videoList:
#        target = os.path.join(directory, video)
#        os.system('omxplayer "{}" > /dev/null'.format(target))

playEpisode()
button = Button(buttonPin)
button.when_released = playEpisode
pause()
