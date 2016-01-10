import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR_PIN1 = 7
PIR_PIN2 = 2

GPIO.setup(PIR_PIN1, GPIO.IN)
#GPIO.setup(PIR_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN2, GPIO.IN)
time_stamp = time.time()

def MOTION1(PIR_PIN1):
	print "Sensor 1 activated!"

def MOTION2(PIR_PIN2):
	global time_stamp
	time_now = time.time()
	if (time_now - time_stamp) >= 1:
		print "Sensor 2 activated"
	time_stamp = time_now

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "READY"

GPIO.add_event_detect(PIR_PIN2, GPIO.RISING, callback=MOTION2)
try:
	GPIO.add_event_detect(PIR_PIN1, GPIO.RISING, callback=MOTION1)
#	GPIO.add_event_detect(PIR_PIN2, GPIO.RISING, callback=MOTION2)
	
	while 1:
		time.sleep(100)

except KeyboardInterrupt:
	print "QUIT"
	GPIO.cleanup()

GPIO.cleanup()
