import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED OFF"
GPIO.output(18,0)

while 1:
	print "LED on"
	GPIO.output(18,1)
	time.sleep(1)
	print "LED off"
	GPIO.output(18,0)

#EoF
