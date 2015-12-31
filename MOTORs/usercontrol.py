import RPi.GPIO as GPIO
from time import sleep
import sys
import Tkinter as tk
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 19
Motor2B = 21
Motor2E = 23

def init(): 
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)

def forward(tf):
#	init()
	print "Going forwards"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
 
	sleep(tf)
	GPIO.cleanup()
 
def reverse(tf):
#	init()
	print "Going backwards"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
 
	sleep(tf)
 	GPIO.cleanup()

def turn_left(tf):
	init()
	print "Take a Left Turn"
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor1B, GPIO.LOW)
	GPIO.output(Motor1E, GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

	sleep(tf)
	GPIO.cleanup()

def turn_right(tf):
#        init()
	print "Take a Right Turn"
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

        sleep(tf)
        GPIO.cleanup()

def pivot_left(tf):
#        init()
	print "Take a Pivot Left Turn"
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)

        sleep(tf)
        GPIO.cleanup()

def pivot_right(tf):
#        init()
	print "Take a Pivot Right Turn"
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

        sleep(tf)
        GPIO.cleanup()

def key_input(event):                                                            
	init()                                                                       
	print 'Key:', event.char                                                     
	key_press = event.char                                                       
	sleep_time = 0.030                                                           
	if key_press.lower() == 'w':                                                 
		forward(sleep_time)                                                      
    	elif key_press.lower() == 's':                                               
        	reverse(sleep_time)                                                      
	elif key_press.lower() == 'a':                                               
		turn_left(sleep_time)                                                    
	elif key_press.lower() == 'd':                                               
		turn_right(sleep_time)                                                   
	elif key_press.lower() == 'q':                                               
		pivot_left(sleep_time)                                                   
	elif key_press.lower() == 'e':                                               
		pivot_right(sleep_time)                                                  
	else:
		GPIO.cleanup()                                                                        
                                                                                 
command = tk.Tk()                                                                
command.bind('<KeyPress>', key_input)                                            
command.mainloop()

def disable_motors():
	print "Now stop"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.cleanup()


#init()
#forward(1)
#reverse(1)
#turn_left(1)
#turn_right(1)
#pivot_left(1)
#pivot_right(1)
