from tkinter import *
import tkinter as tk

from code_body import general_control_text as gntext
from code_body import general_control_ON as gnON


def my_body(window):
    # -------------------------------- Titulo Zona Boton General --------------------------------
    tittle = Label(window, text="Tablero de Control Principal",bg="#FFFFFF", font="Helvetica 14", fg="#000000", height=2)
    tittle.grid(row=2, column=0, columnspan=2)
    # -------------------------------- Titulos de Controles --------------------------------
    gntext.body_gncontrol_text(window)
    # -------------------------------- Botones de Encendido --------------------------------
    gnON.body_gncontrol_buttonON(window)
    # -------------------------------- Botonoes de Apagado --------------------------------


    # -------------------------------- Titulo Zona Control Tiempos --------------------------------

    # -------------------------------- Titulo Zona Muestra de tiempo transcurrido (OJO) --------------------------------
# boton de parada y start
    # -------------------------------- Titulo Zona Alertas (Inferior) --------------------------------
