import sys
import time
import os
import time
import RPi.GPIO as GPIO


StepPin = 23
DirPin = 24
x = 0
pause = 0.005  #0.001
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(StepPin, GPIO.OUT)
GPIO.setup(DirPin, GPIO.OUT)

while x <= 5:
    print(x)
    x = x + 1
    i = 0
    j = 0

    time.sleep(1)
    GPIO.output(DirPin, GPIO.HIGH)

    while i <= 250:
        i = i + 1
        GPIO.output(StepPin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(StepPin, GPIO.LOW)
        time.sleep(pause)
        
    time.sleep(.5)
    GPIO.output(DirPin, GPIO.LOW)

    while j <= 250:
        j = j + 1
        GPIO.output(StepPin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(StepPin, GPIO.LOW)
        time.sleep(pause)
