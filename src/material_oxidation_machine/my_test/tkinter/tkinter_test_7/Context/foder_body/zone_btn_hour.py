from tkinter import *
import tkinter as tk

from folder_helps import check

def btn_hour(window, hourmin, hourmax, df_sensors):

    #titulo que mecione lo que se debe ingresar
    enunciado = Label(window, text="A continuacion debe ingresar el rango de tiempo que \n"+ 
                                    "quiere vizualizar de los datos registrados por los \n"+
                                    "sensores de la Maquina de Niebla Salina"
                      ,bg="#76D7C4", font="Helvetica 12", fg="#000000", height=4)
    #entrada hora minima
    tittle_1 = Label(window, text="Hora Minima(24h): ", bg="#76D7C4", font="Helvetica 12", fg="#000000", height=2, justify="left")
    in_hour_min = Entry(window, font="Helvetica 14", width=10, justify="center")
    # #entrada hora maxima
    tittle_2 = Label(window, text="Hora Maxima(24h): ",bg="#76D7C4", font="Helvetica 12", fg="#000000", height=2, justify="left")
    in_hour_max = Entry(window, font="Helvetica 14", width=10, justify="center")

    btn_graph = Button(window, text=" GRAFICAR \n SENSORES ", font="Helvetica 14", bg="#2ECC71", fg="#145A32", width="20",height=3
                       ,command= lambda: check.check_hourrange(window, hourmin, in_hour_min, hourmax, in_hour_max, df_sensors) )

    enunciado.grid(row=13, column=7,  columnspan=17)

    tittle_1.grid(row=14, column=7, columnspan=17)
    in_hour_min.grid(row=14, column=13,  columnspan=17)

    tittle_2.grid(row=15, column=7,  columnspan=17)
    in_hour_max.grid(row=15, column=13,  columnspan=17)

    btn_graph.grid(row=16, column=7,  columnspan=17)