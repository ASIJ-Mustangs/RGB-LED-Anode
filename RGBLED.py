from microbit import *
from random import randint

redVal = 0
greenVal = 255
blueVal = 255

while True:
    if button_a.is_pressed():
        redVal = 255
        blueVal = 255
        greenVal = 0
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    elif button_b.is_pressed():
        redVal = 255
        blueVal = 0
        greenVal = 255
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    else:
        pin0.write_analog(redVal)
        pin1.write_analog(greenVal)
        pin2.write_analog(blueVal)
    redVal = 0
    greenVal = 255
    blueVal = 255
