# https://iot-guider.com/raspberrypi/metal-touch-sensor-module-ky-036-in-raspberry-pi/
# Interfacing Metal Touch Sensor Module KY-036 w/ RPi
import RPi.GPIO as GPIO

TouchPin = 13
LedPin   = 15

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		if GPIO.input(TouchPin) == GPIO.LOW:
			print '...led on'
			GPIO.output(LedPin, GPIO.LOW)  # led on
		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if _name_ == '_main_':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
