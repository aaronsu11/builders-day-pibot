import sys
import time
import RPi.GPIO as GPIO


# GPIO / board initialisation
mode=GPIO.getmode()
GPIO.cleanup()  # start with a cleanup() to make sure we have a clean slate (if this throws a warning, it just means everything was already clean)
GPIO.setmode(GPIO.BCM)

# Setup motor A:
#   GPIO 5 (RPi Pin 29) -> IN1 (Motor A Forward)
#   GPIO 6 (RPi Pin 31) -> IN2 (Motor A Reverse)
a_forward = 5
a_reverse = 6
GPIO.setup(a_forward, GPIO.OUT)
GPIO.setup(a_reverse, GPIO.OUT)


# Setup motor B:
#   GPIO 23 (RPi Pin 16) -> IN3 (Motor B Forward)
#   GPIO 24 (RPi Pin 18)  -> IN4 (Motor B Reverse)
b_forward = 23
b_reverse = 24
GPIO.setup(b_forward, GPIO.OUT)
GPIO.setup(b_reverse, GPIO.OUT)


def run_a_forward(x):
    GPIO.output(a_forward, GPIO.HIGH)
    print("Running Motor A Forward")
    time.sleep(x)
    GPIO.output(a_forward, GPIO.LOW)

def run_b_forward(x):
    GPIO.output(b_forward, GPIO.HIGH)
    print("Running Motor B Forward")
    time.sleep(x)
    GPIO.output(b_forward, GPIO.LOW)

def run_a_reverse(x):
    GPIO.output(a_reverse, GPIO.HIGH)
    print("Running Motor A Reverse")
    time.sleep(x)
    GPIO.output(a_reverse, GPIO.LOW)

def run_b_reverse(x):
    GPIO.output(b_reverse, GPIO.HIGH)
    print("Running Motor B Reverse")
    time.sleep(x)
    GPIO.output(b_reverse, GPIO.LOW)

def all_forward(x):
    GPIO.output(a_forward, GPIO.HIGH)
    GPIO.output(b_forward, GPIO.HIGH)
    print("Moving All Forward")
    time.sleep(x)
    GPIO.output(a_forward, GPIO.LOW)
    GPIO.output(b_forward, GPIO.LOW)

def all_reverse(x):
    GPIO.output(a_reverse, GPIO.HIGH)
    GPIO.output(b_reverse, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(a_reverse, GPIO.LOW)
    GPIO.output(b_reverse, GPIO.LOW)

all_forward(5)
all_reverse(5)

#while (1):   
#    all_forward(5)
#    all_reverse(5)

GPIO.cleanup()
