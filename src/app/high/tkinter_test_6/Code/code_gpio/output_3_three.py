# Hornillo y toma disponible AC.

# Todo el sistema de a maquina de niebla salina
import RPi.GPIO as GPIO
import time

#--------------------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD)

pin2 = 38 #GPIO 20
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2,0)

#---------------------------------------Menu de encendido ------------------------------------
def output_on(number):
    if number == 3:
        time.sleep(1)
        GPIO.output(pin2, 1)
        print("salida 3 se ha encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 2")
#--------------------------------------Menu de Apagado----------------------------------------
def output_off(number):
    if number == 3:
        time.sleep(1)
        GPIO.output(pin2, 0)
        print("Salida 3 se ha apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 2")