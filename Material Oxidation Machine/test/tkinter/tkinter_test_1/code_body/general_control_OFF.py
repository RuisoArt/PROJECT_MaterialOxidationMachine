from tkinter import *
import tkinter as tk

def body_gncontrol_buttonOFF(window):
# OJO! que falta los comandos agregados paraencender la maquina, unir a los modulos de control de CLI
    control_1 = Button(window, text="[1] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_2 = Button(window, text="[2] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_3 = Button(window, text="[3] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_4 = Button(window, text="[4] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_5 = Button(window, text="[5] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_6 = Button(window, text="[6] OFF ", font="Helvetica 12", bg="#FF0055", fg="white") 
    control_7 = Button(window, text="[7] OFF ", font="Helvetica 12", bg="#FF0055", fg="white")

    control_1.grid(row=4, column=2)
    control_2.grid(row=5, column=2)
    control_3.grid(row=6, column=2)
    control_4.grid(row=7, column=2)
    control_5.grid(row=8, column=2)
    control_6.grid(row=9, column=2)
    control_7.grid(row=10, column=2) 
    