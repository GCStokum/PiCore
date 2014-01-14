import sys
import time
import os
import time
import RPIO as GPIO


StepPin = 18
DirPin = 17
x = 0
pause = 0.001
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while x <= 10:
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
    time.sleep(1)
    GPIO.output(DirPin, GPIO.LOW)
    while j <= 500:
        j = j + 1
        GPIO.output(StepPin, GPIO.HIGH)
        time.sleep(pause)
        GPIO.output(StepPin, GPIO.LOW)
        time.sleep(pause)


