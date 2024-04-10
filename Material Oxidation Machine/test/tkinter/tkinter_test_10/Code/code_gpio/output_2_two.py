# Luminarias Traseras
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin1 = 36 #GPIO 16
GPIO.setup(pin1, GPIO.OUT)
GPIO.output(pin1,0)

def output_on(number):
    if number == 2:
        time.sleep(1)
        GPIO.output(pin1, 1)
        print("La Salida 2 se ha encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 1")

def output_off(number):
    if number == 2:
        time.sleep(1)
        GPIO.output(pin1, 0)
        print("La Salida 2 se ha apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 1")