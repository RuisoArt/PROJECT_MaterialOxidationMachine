#Luminarias Delanteras
import RPi.GPIO as GPIO
#pip install GPIOSimulator
#pip install RPi.GPIO
#python.exe -m pip install --upgrade pip
import time

GPIO.setmode(GPIO.BOARD)

pin0 = 32 #GPIO 12 
GPIO.setup(pin0, GPIO.OUT)
GPIO.output(pin0,0)

def output_on(number):
    if number == 1:
        time.sleep(1)
        GPIO.output(pin0, 1)
        print("La Salida 1 se ha encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0")

def output_off(number):
    if number == 1:
        time.sleep(1)
        GPIO.output(pin0, 0)
        print("La Salida 1 se ha apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0")