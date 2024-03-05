import time
import sensors.models.PIN_GPIO as gpio
from gpiozero import LED

class GPIO_behaviour():
    def security_init_pin():
        gpio.PIN_GPIO.output_15.off() # buena practica que proteje el harware, iniciar con los pines apagados

    def encender_pin_15():
        print("............................................")
        print("Se inicia el led 15")
        print("comprueba en la salida de la raspberry")
        print("............................................")
        gpio.PIN_GPIO.output_15.on()
        
    def apagar_pin_15():
        print("............................................")
        print("Se apaga el led 15")
        print("comprueba en la salida de la raspberry")
        print("............................................")
        gpio.PIN_GPIO.output_15.off()