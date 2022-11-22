import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED 1 RED

GPIO.setup(17,GPIO.OUT)


GPIO.output(17,GPIO.HIGH)

time.sleep(1)

GPIO.output(17,GPIO.LOW)

#LED 2 YELLOW

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.OUT)


GPIO.output(10,GPIO.HIGH)

time.sleep(1)

GPIO.output(10,GPIO.LOW)

#LED 3 GREEEN

GPIO.setup(11,GPIO.OUT)


GPIO.output(11,GPIO.HIGH)

time.sleep(1)

GPIO.output(11,GPIO.LOW)