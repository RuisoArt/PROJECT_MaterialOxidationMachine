# En terminal: sudo pip install --upgrade RPi.GPIO
import RPi.GPIO as GPIO
#from gpiozero import AnalogInputDevice as an
import time

GPIO.setmode(GPIO.BOARD)

#Variable pulsador en pull up, cuando se preciona es un 0, estado normal en 1(3v3)
push = 18 #GPIO 24 

GPIO.setup(push,GPIO.IN)

while 1:
    lec_push = GPIO.input(push)

    if lec_push == 0:
        print("Se esta presionando el pulsador")
    else:
        print("No se esta pulsando el pulsador")