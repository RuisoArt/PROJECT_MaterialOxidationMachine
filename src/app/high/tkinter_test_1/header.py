from tkinter import *
import tkinter as tk

from code_header import grid_random as grd

def my_header(window):
    # ----------------------------------------------------------------guia de grilla
    grd.header_grid_random(window)
    # ----------------------------------LOGOS------------------------------
    relative_route = str("app/high/tkinter_test_1/")

    img_rasplogo = PhotoImage(file= relative_route + "assets/img/COLOURRaspberryPI.png")
    img_ustalogo = PhotoImage(file= relative_route + "assets/img/logo.png")

    sm_img_rasp = img_rasplogo.subsample(5,5)
    sm_img_usta = img_ustalogo.subsample(5,5)

    img_rasp = Label(window, image = sm_img_rasp, bg="#FFFFFF", width="150")
    img_usta = Label(window, image = sm_img_usta, bg="#FFFFFF", width="150")

    img_rasp.grid(row=1, column=0)
    img_usta.grid(row=1, column=19)
    # -----------------------------------TITULOS----------------------------------
    tittle_primary = Label(window, text = "Software de Control Maquina de Niebla Salina"
                                    +" - Facultad de Ingenieria Mecanica"
                                    +"\nLaboratorio de Materiales"
                                    , bg="#FFFFFF", font="Helvetica 16", fg="#000000", height=3)
    tittle_secundary = Label(window, text = "Proyecto Desarrollado por Ingenieros Electronicos, Mecanicos y de Sistemas de la Universidad Santo Tomas seccional Tunja."
                            , bg="#FFFFFF", font="Helvetica 10", fg="#000000", height=2)

    tittle_primary.grid(row=1, column=1, columnspan=18)
    tittle_secundary.grid(row=2, column=0, columnspan=19)

