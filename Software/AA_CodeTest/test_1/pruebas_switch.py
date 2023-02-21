from gpiozero import LED
from time import sleep

# Lateral de la raspberry extension
array_leds = [18, 23, 24, 25, 12, 16, 20, 21]
contador = 0
loop_max = int( input("Cuantos ciclos maximos: ") )

while(True):
    for i in range(len(array_leds)):
        led = LED(array_leds[i])
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
    contador += 1
    if contador == loop_max: break