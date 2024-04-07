from tkinter import *
import tkinter as tk

from code_gpio import output_1_one as output1
from code_gpio import output_2_two as output2
from code_gpio import output_3_three as output3
from code_gpio import output_4_four as output4
from code_gpio import output_5_five as output5
from code_gpio import output_6_six as output6
from code_gpio import output_7_seven as output7

# ------------------------------- Control de apagado ----------------------------------------
def gpio_off(number):
    
    if number == 1:
        output1.output_off(1)
    elif number == 2:
        output2.output_off(2)
    elif number == 3:
        output3.output_off(3)
    elif number == 4:
        output4.output_off(4)
    elif number == 5:
        output5.output_off(5)
    elif number == 6:
        output6.output_off(6)
    elif number == 7:
        output7.output_off(7)
    else:
        print("No es un boton, error")
# -------------------------------- Menu de apagado ------------------------------------------
def body_gncontrol_buttonOFF(window):
# OJO! que falta los comandos agregados paraencender la maquina, unir a los modulos de control de CLI
    control_1 = Button(window, text="[1] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(1)) 
    control_2 = Button(window, text="[2] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(2)) 
    control_3 = Button(window, text="[3] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(3)) 
    control_4 = Button(window, text="[4] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(4)) 
    control_5 = Button(window, text="[5] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(5)) 
    control_6 = Button(window, text="[6] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(6)) 
    control_7 = Button(window, text="[7] OFF ", font="Helvetica 12", bg="#FF0055", fg="white"
                       , command= lambda: gpio_off(7))

    control_1.grid(row=4, column=2)
    control_2.grid(row=5, column=2)
    control_3.grid(row=6, column=2)
    control_4.grid(row=7, column=2)
    control_5.grid(row=8, column=2)
    control_6.grid(row=9, column=2)
    control_7.grid(row=10, column=2) 
    