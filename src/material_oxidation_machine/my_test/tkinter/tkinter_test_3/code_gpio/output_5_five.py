# Todas las luminarias

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin0 = 32 #GPIO 12   
GPIO.setup(pin0, GPIO.OUT)
GPIO.output(pin0,0)

pin1 = 36 #GPIO 16   
GPIO.setup(pin1, GPIO.OUT)
GPIO.output(pin1,0)

def output_on(number):
    if number == 5:
        time.sleep(1)
        GPIO.output(pin0, 1)
        time.sleep(1)
        GPIO.output(pin1, 1)
        print("La Salida 1 y 2 se han encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0 y 1")

def output_off(number):
    if number == 5:
        time.sleep(1)
        GPIO.output(pin0, 0)
        time.sleep(1)
        GPIO.output(pin1, 0)
        print("La Salida 1 y 2 se ha apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0 y 1")
