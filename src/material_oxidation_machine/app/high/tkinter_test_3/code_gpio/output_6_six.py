# Todo sistema de conmutacion de alta potencia, hornillo, resistencia, compresor, toma disponible.

# Todo el sistema de a maquina de niebla salina
import RPi.GPIO as GPIO
import time

#--------------------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD)

pin2 = 38 #GPIO 20
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2,0)

pin3 = 40 #GPIO 21 
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3,0)
#---------------------------------------Menu de encendido ------------------------------------
def output_on(number):
    if number == 6:
        time.sleep(0.25)
        GPIO.output(pin2, 1)
        time.sleep(0.25)
        GPIO.output(pin3, 1)
        print("Salida 6 encendida")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 2 al 3")
#--------------------------------------Menu de Apagado----------------------------------------
def output_off(number):
    if number == 6:
        time.sleep(0.25)
        GPIO.output(pin2, 0)
        time.sleep(0.25)
        GPIO.output(pin3, 0)
        print("Salida 6 apagada")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 2 al 3")