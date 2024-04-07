# En terminal: sudo pip install --upgrade RPi.GPIO
import RPi.GPIO as GPIO
#from gpiozero import AnalogInputDevice as an
import time

GPIO.setmode(GPIO.BOARD)

led_1 = 32 #GPIO 12
led_2 = 36 #GPIO 16
led_3 = 38 #GPIO 20
led_4 = 40 #GPIO 21

GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.setup(led_3,GPIO.OUT)
GPIO.setup(led_4,GPIO.OUT)

while True:
    estado = int( input("estado: ") )

    GPIO.output(led_1,estado)
    GPIO.output(led_2,estado)
    GPIO.output(led_3,estado)
    GPIO.output(led_4,estado)