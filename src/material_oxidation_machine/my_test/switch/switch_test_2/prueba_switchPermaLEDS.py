# En terminal: sudo pip install --upgrade RPi.GPIO
import RPi.GPIO as GPIO
#from gpiozero import AnalogInputDevice as an
import time

# Este codigo parte de un pulsador en pull up (interruptor de pin xx a GND y resistencia a pin xx)

GPIO.setmode(GPIO.BOARD)

#Variable pulsador en pull up, cuando se preciona es un 0, estado normal en 1(3v3)
push = 18 #GPIO 24
led_1 = 32 #GPIO 12
led_2 = 36 #GPIO 16
led_3 = 38 #GPIO 20
led_4 = 40 #GPIO 21

GPIO.setup(push,GPIO.IN)
GPIO.setup(led_1,GPIO.OUT)
GPIO.setup(led_2,GPIO.OUT)
GPIO.setup(led_3,GPIO.OUT)
GPIO.setup(led_4,GPIO.OUT)

estado_led = 0
estado_anterior = 0

while 1:
    lec_push = GPIO.input(push)


    if (not lec_push) == 1 and estado_anterior == 0:
        estado_led = 1 - estado_led
        print("Se esta presionando el pulsador")
        time.sleep(0.01)
    estado_anterior = not lec_push
    if estado_led == 1:
        
        GPIO.output(led_1,1)
        time.sleep(0.5)
        GPIO.output(led_2,1)
        time.sleep(0.5)
        GPIO.output(led_3,1)
        time.sleep(0.5)
        GPIO.output(led_4,1)
        time.sleep(0.5)
    else:
        print("No se esta pulsando el pulsador")
        GPIO.output(led_1,0)
        GPIO.output(led_2,0)
        GPIO.output(led_3,0)
        GPIO.output(led_4,0)