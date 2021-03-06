# SparkFun Electronics
# Experiment 4.0
# Driving an RGB LED
# Common anode RGB LED

from microbit import *
from random import randint

redVal = 0
greenVal = 1023
blueVal = 1023

while True:
    if button_a.is_pressed():
        redVal = 1023
        blueVal = 1023
        greenVal = 0
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    elif button_b.is_pressed():
        redVal = 1023
        blueVal = 0
        greenVal = 1023
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    else:
        redVal = 0
        greenVal = 1023
        blueVal = 1023
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
