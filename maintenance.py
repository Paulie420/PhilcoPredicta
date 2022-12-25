#!/usr/bin/python

import os

#print('Removing nohup files . . .')
os.system('clear')
#os.system('/usr/bin/fbi -T 1 -noverbose -a /etc/splash.png')
os.system('rm /home/pi/nohup.out')
#print('Starting Predicta.py - Lets r0ck this j0int . . .')
os.system('python3 /home/pi/predicta.py')

