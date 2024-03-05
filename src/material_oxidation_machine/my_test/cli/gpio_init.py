import RPi.GPIO as GPIO
import time

def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    pin0 = 32 #GPIO 12   compresor, resistencia
    pin1 = 36 #GPIO 16   hornillo, toma disponible
    pin2 = 38 #GPIO 20   luminarias delanteras
    pin3 = 40 #GPIO 21   luminarias traseras

    GPIO.setup(pin0, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)

    GPIO.output(pin0,0)
    GPIO.output(pin1,0)
    GPIO.output(pin2,0)
    GPIO.output(pin3,0)

    return pin0, pin1, pin2, pin3
