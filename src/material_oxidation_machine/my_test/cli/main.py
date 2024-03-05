import RPi.GPIO as GPIO
import time

from gpio_init import init_gpio
from text import warning_text
from text import menu_text
from keyboard_init import my_keyboard
from keyboard_onoff import my_decition as decition
from onoff import output_ZERO as ZERO
from onoff import output_ONE as ONE
from onoff import output_TWO as TWO
from onoff import output_THREE as THREE

pin0, pin1, pin2, pin3 = init_gpio() #inicializara la configuracion y estado inicial de los puertos
warning_text() #inicializa aviso inicial por 3 segundos

def menu_main():
    menu_text() #iniciaiza el menu inicial por 2 segundos

    while True:
        print("---------------------------------------------------------------")
        key = my_keyboard()

        if key == 0:
            print("\n\n\n---------------------------------------------------------------")
            print("---------------------------------------------------------------")
            print("Saldra del menu de conmutacion.")
            print("---------------------------------------------------------------")
            break
        
        elif key == 1:
            conm = decition()
            ZERO(conm)

        elif key == 2:
            conm = decition()
            ONE(conm)

        elif key == 3:
            conm = decition()
            ZERO(conm)
            ONE(conm)

        elif key == 4:
            conm = decition()
            TWO(conm)

        elif key == 5:
            conm = decition()
            THREE(conm)

        elif key == 6:
            conm = decition()
            TWO(conm)
            THREE(conm)

        elif key == 7:
            conm = decition()
            ZERO(conm)
            ONE(conm)
            TWO(conm)
            THREE(conm)

        else:
            print("Opcion Invalida")

menu_main()
