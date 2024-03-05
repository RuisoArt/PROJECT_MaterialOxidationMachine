from gpiozero import LED
from gpiozero import Button
from time import sleep

array_leds = [23, 24, 25, 12, 16, 20, 21]
pulsador = Button(18)

pulsador.wait_for_inactive()
print("Se desactivo el pin")

for i in range(len(array_leds)):
    led = LED(array_leds[i])
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)