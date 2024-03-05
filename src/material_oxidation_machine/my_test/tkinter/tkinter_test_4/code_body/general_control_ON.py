from tkinter import *
import tkinter as tk

from code_gpio import output_1_one as output1
from code_gpio import output_2_two as output2
from code_gpio import output_3_three as output3
from code_gpio import output_4_four as output4
from code_gpio import output_5_five as output5
from code_gpio import output_6_six as output6
from code_gpio import output_7_seven as output7

# ------------------------------- Control de encendido ----------------------------------------
def gpio_on(number):
    
    if number == 1:
        output1.output_on(1)
    elif number == 2:
        output2.output_on(2)
    elif number == 3:
        output3.output_on(3)
    elif number == 4:
        output4.output_on(4)
    elif number == 5:
        output5.output_on(5)
    elif number == 6:
        output6.output_on(6)
    elif number == 7:
        output7.output_on(7)
    else:
        print("No es un boton, error")
# -------------------------------- Menu de encendido ------------------------------------------
def body_gncontrol_buttonON(window):
# OJO! que falta los comandos agregados paraencender la maquina, unir a los modulos de control de CLI
    control_1 = Button(window, text="[1] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(1)) 
    control_2 = Button(window, text="[2] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(2)) 
    control_3 = Button(window, text="[3] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(3)) 
    control_4 = Button(window, text="[4] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(4)) 
    control_5 = Button(window, text="[5] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(5)) 
    control_6 = Button(window, text="[6] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(6)) 
    control_7 = Button(window, text="[7] ON ", font="Helvetica 12", bg="#2ECC71", fg="white"
                       , command= lambda: gpio_on(7))

    control_1.grid(row=4, column=1)
    control_2.grid(row=5, column=1)
    control_3.grid(row=6, column=1)
    control_4.grid(row=7, column=1)
    control_5.grid(row=8, column=1)
    control_6.grid(row=9, column=1)
    control_7.grid(row=10, column=1) 
    