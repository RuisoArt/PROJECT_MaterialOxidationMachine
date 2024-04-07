import RPi.GPIO as GPIO

from gpio_init import init_gpio

pin0, pin1, pin2, pin3 = init_gpio()

def output_ZERO(VAR):
    if VAR == 1:
        GPIO.output(pin0, 1)
    elif VAR == 2:
        GPIO.output(pin0, 0)
    else:
        print("Invalid response output ZERO")

def output_ONE(VAR):
    if VAR == 1:
        GPIO.output(pin1, 1)
    elif VAR == 2:
        GPIO.output(pin1, 0)
    else:
        print("Invalid response output ONE")

def output_TWO(VAR):
    if VAR == 1:
        GPIO.output(pin2, 1)
    elif VAR == 2:
        GPIO.output(pin2, 0)
    else:
        print("Invalid response output TWO")

def output_THREE(VAR):
    if VAR == 1:
        GPIO.output(pin3, 1)
    elif VAR == 2:
        GPIO.output(pin3, 0)
    else:
        print("Invalid response output THREE")