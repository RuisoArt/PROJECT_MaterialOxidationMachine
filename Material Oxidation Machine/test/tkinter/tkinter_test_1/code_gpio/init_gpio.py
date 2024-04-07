import RPi.GPIO as GPIO
#pip install GPIOSimulator
#pip install RPi.GPIO
#python.exe -m pip install --upgrade pip
import time


def init_gpio():
    GPIO.setmode(GPIO.BOARD)

    # Son cuatro salidas de conmutacion que disparan 7 outputs fisicos encendidos
    pin0 = 32 #GPIO 12   compresor, resistencia
    pin1 = 36 #GPIO 16   hornillo, toma disponible
    pin2 = 38 #GPIO 20   luminarias delanteras
    pin3 = 40 #GPIO 21   luminarias traseras

    GPIO.setup(pin0, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)

    config_0 = GPIO.output(pin0,0)
    config_1 = GPIO.output(pin1,0)
    config_2 = GPIO.output(pin2,0)
    config_3 = GPIO.output(pin3,0)

    return [config_0, config_1, config_2, config_3]
