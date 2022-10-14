import sys
import time
import RPi.GPIO as GPIO
mode=GPIO.getmode()
GPIO.cleanup()
# GPIO 5 (29) -> IN1
# GPIO 6 (31) -> IN2
Forward=29
Backward=31
sleeptime=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)
def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)
while (1):
    
    forward(5)
    reverse(5)
GPIO.cleanup()
