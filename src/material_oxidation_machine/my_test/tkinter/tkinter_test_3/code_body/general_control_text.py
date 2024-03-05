from tkinter import *
import tkinter as tk

def body_gncontrol_text(window):
    tittle_1 = Label(window, text="Tablero de Control Principal",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_1.grid(row=3, column=0, columnspan=1)

    mood_1 = Label(window, text="[1] Luminarias Delanteras", font="Helvetica 12", fg="#000000", height=2)
    mood_2 = Label(window, text="[2] Luminarias Traseras", font="Helvetica 12", fg="#000000", height=2)
    mood_3 = Label(window, text="[3] Hornillo y Toma AC", font="Helvetica 12", fg="#000000", height=2)
    mood_4 = Label(window, text="[4] Compresor de Aire y \nSistema de Neblina Acida \n (Resistor Sumergible)", font="Helvetica 12", fg="#000000", height=4)
    mood_5 = Label(window, text="[5] Todas las Luminarias", font="Helvetica 12", fg="#000000", height=2)
    mood_6 = Label(window, text="[6] Todo el sistema de Potencia", font="Helvetica 12", fg="#000000", height=2)
    mood_7 = Label(window, text="[7] Todo el sistema", font="Helvetica 12", fg="#000000", height=2)

    mood_1.grid(row=4, column=0)
    mood_2.grid(row=5, column=0)
    mood_3.grid(row=6, column=0)
    mood_4.grid(row=7, column=0)
    mood_5.grid(row=8, column=0)
    mood_6.grid(row=9, column=0)
    mood_7.grid(row=10, column=0)
