#!/usr/bin/python

# Needed libraries
import os
import random
import time
import subprocess
from gpiozero import Button
from signal import pause

# Setup Raspberry Pi Pin / Video Directory
buttonPin = 21
directory = "/home/pi/Videos/"

process = None

# Function that plays a random video
def playEpisode():
    global process
    if not os.path.exists(directory) or not os.listdir(directory):
        print('Directory does not exist or is empty.')
        return
    # Select a random video
    episode = directory + random.choice(os.listdir(directory))
    # Kill old omxplayer instances
    os.system('sudo pkill omxplayer')
    # Play video
    process = subprocess.Popen(["omxplayer", "--aspect-mode", "stretch", episode], stdout=subprocess.PIPE)

# Function to check when omxplayer finishes playing a video
def check_omxplayer():
    global process
    if process is not None and process.poll() is not None:
        playEpisode()

# Display images at startup; last image shows on screen when videos switch
def displayImage():
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "-a", "/home/pi/Pics/logo_philco_1920px.svg.png"])
    time.sleep(7)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "/home/pi/Pics/Philco_Predicta_600_lq_0009.jpg"])
    time.sleep(1.6)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "/home/pi/Pics/Philco_Predicta_600_lq_0008.jpg"])
    time.sleep(1.6)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "/home/pi/Pics/Philco_Predicta_600_lq_0007.jpg"])
    time.sleep(1.6)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "/home/pi/Pics/Philco_Predicta_600_lq_0006.jpg"])
    time.sleep(1.6)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "/home/pi/Pics/Philco_Predicta_600_lq_0005.jpg"])
    time.sleep(1)
    subprocess.run(["sudo", "fbi", "-T", "2", "-noverbose", "-a", "/home/pi/Pics/philco_predicta_holiday.jpg"])
    time.sleep(4)


# Lets run the thing!
displayImage()
playEpisode()

# Listens for button presses (releases, actually)
button = Button(buttonPin)
button.when_released = playEpisode

# Checks if omxplayer is running / has ended
while True:
    check_omxplayer()
    time.sleep(1)

