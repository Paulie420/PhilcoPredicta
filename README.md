# PhilcoPredicta
Philco Predicta Project using a capacitive touch sensor to play random videos 
on an antique television. 

I have a 1942 Philco Predicta television. It is black & white and requires a 
75 Ohm to 300 Ohm UHF/VHF/FM Matching Transformer Converter Adapter to get from 
its two pronged connection to a coaxial cable connection. It also requires an 
HDMI to coaxial convertor.

I'm using a Raspberry Pi Zero and a capacitive touch sensor. I chose a
capacitive touch sensor so that I didn't have to physically modify the Predicta
at all; the capacitive touch sensor is set off through the wooden frame from
inside the Predicta.

The python code displays a few Philco Predicta Holiday (model) images before
starting to play random videos. If nothing else happens, it will continue to
play random videos from a directory that can be set in the code. If the user
presses (or actually when they release) a capacative touch sensor, a new random
video plays.

Rinse, repeat.

I'd like to add more features, like playing a couple commericials after every
third random video so the experience is more like regular televsion from that
period.

Way down the line, maybe theres a way to have some sort of menu or more buttons
in order to do more specific things; like play I Love Lucy or All in the Family
exclusively... or just have more options for selecting WHAT videos to play.

Maybe we could add Pong. Currently, I use no external device for input - we use
only a capacitve touch sensor; if we add Pong, what input devices could be 
used to make a better/more expansive feature set?

This is intended to give more functionality to an old television that doesn't
work as it was designed anymore. Obviously, it uses UHF/VHF like all the 
original televisions - but with my mods you can run any HDMI source thru it - 
however this project IS the source; so the end user just turns on the Predicta 
and it starts playing videos. This gives the Predicta new life... theres many 
applications for old antique televisions, and I hope to expand this project 
into something that is good for all antique televisions.
----
If you wanted to install yourself, just install Raspberry Pi OS Lite to a 
Raspberry Pi Zero (or other).

sudo apt update
sudo apt upgrade
sudo apt install omxplayer fbi

And add a cronjob to run the script;
sudo crontab -e

And add the following line;
@reboot python2 /home/pi/maintenance.py
-----
Reboot the Pi and the script will begin. Install a capacative touch sensor on
Pin 21. A button can be used, but you would have to change the Python code to
call button.when_pressed instead of button.when_released .

