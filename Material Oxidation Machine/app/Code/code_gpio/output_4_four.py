# compresor de aire y resistencia sumerjible
# Todo el sistema de a maquina de niebla salina
import RPi.GPIO as GPIO
import time

#--------------------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD)
pin3 = 40 #GPIO 21 
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3,0)
#---------------------------------------Menu de encendido ------------------------------------
def output_on(number):
    if number == 4:
        time.sleep(1)
        GPIO.output(pin3, 1)
        print("Salida 4 se ha encendido")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 3")
#--------------------------------------Menu de Apagado----------------------------------------
def output_off(number):
    if number == 4:
        time.sleep(1)
        GPIO.output(pin3, 0)
        print("Salida 4 se ha apagado")
    else:
        print("No ha llegado lo que se solicuta para encender el pin 3")
