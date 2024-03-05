from gpiozero import LED
from time import sleep

led = LED(15)

estado = int (input("Cuantas veces quieres que se encienda ya apague el led: "))
for i in range(estado):
    led.on()
    sleep(1)
    led.off()
    sleep(1)