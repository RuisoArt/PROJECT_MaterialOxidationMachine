# Todo el sistema de a maquina de niebla salina
import RPi.GPIO as GPIO
import time

#--------------------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD)

pin0 = 32 #GPIO 12 
GPIO.setup(pin0, GPIO.OUT)
GPIO.output(pin0,0)

pin1 = 36 #GPIO 16
GPIO.setup(pin1, GPIO.OUT)
GPIO.output(pin1,0)

pin2 = 38 #GPIO 20
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2,0)

pin3 = 40 #GPIO 21 
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3,0)
#---------------------------------------Menu de encendido ------------------------------------
def output_on(number):
    if number == 7:
        time.sleep(0.25)
        GPIO.output(pin0, 1)
        time.sleep(0.25)
        GPIO.output(pin1, 1)
        time.sleep(0.25)
        GPIO.output(pin2, 1)
        time.sleep(0.25)
        GPIO.output(pin3, 1)
        print("Todas las salidas se han encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0 al 3")
#--------------------------------------Menu de Apagado----------------------------------------
def output_off(number):
    if number == 7:
        time.sleep(0.25)
        GPIO.output(pin0, 0)
        time.sleep(0.25)
        GPIO.output(pin1, 0)
        time.sleep(0.25)
        GPIO.output(pin2, 0)
        time.sleep(0.25)
        GPIO.output(pin3, 0)
        print("Todas las salidas se han apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 0 al 3")