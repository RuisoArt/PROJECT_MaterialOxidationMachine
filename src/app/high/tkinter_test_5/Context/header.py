from tkinter import *
import tkinter as tk

from folder_helps import grid_random as grd

def my_second_header(window):
    grd.header_grid_random(window)
    # -----------------------------------TITULOS----------------------------------
    tittle_primary = Label(window, text = "Software de Control Maquina de Niebla Salina"
                                    +" - Facultad de Ingenieria Mecanica"
                                    +"\nLaboratorio de Materiales"
                                    +"\nHistorial de resgistro de Sensores"
                                    , font="Helvetica 16", fg="#000000", height=3)
    tittle_secundary = Label(window, text = "Proyecto Desarrollado por Ingenieros Electronicos, Mecanicos y de Sistemas de la Universidad Santo Tomas seccional Tunja."
                            , font="Helvetica 10", fg="#000000", height=2, justify="center")

    tittle_primary.grid(row=1, column=1, columnspan=18)
    tittle_secundary.grid(row=2, column=1, columnspan=18)
    

