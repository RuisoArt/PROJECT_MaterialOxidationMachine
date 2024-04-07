from tkinter import *
import tkinter as tk
import time

def window_reverse_count(window, minutos, segundos, restante):
    tittle = Label(window, text=" Tiempo en Proceso " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2, width=20)
    tittle.grid(row=3, column=16, columnspan=18)

    show = Label(window, text=  "Tiempo Total: "+str(minutos)+"\n"
                                "Tiempo en Segundos: "+str(segundos)+" s\n"
                                "Tiempo Restante: "+str(restante)+" s"
                                ,bg="#82E0AA", font="Helvetica 12", fg="#000000",)
    show.grid(row=4, rowspan=5, column=16, columnspan=18)

    

def finished_window(window):
    tittle = Label(window, text=" Tiempo en Proceso " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2, width=20)
    tittle.grid(row=3, column=16, columnspan=18)

    show = Label(window, text=  "Ejecucion Terminada"
                                ,bg="#FF0000", font="Helvetica 12", fg="#000000", height=2)
    show.grid(row=5, rowspan=7, column=16, columnspan=18)

