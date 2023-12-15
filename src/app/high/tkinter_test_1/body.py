from tkinter import *
import tkinter as tk

from code_body import general_control_text as gntext
from code_body import general_control_ON as gnON
from code_body import general_control_OFF as gnOFF
from code_body import time_control as tmbtn
from code_config import count as cnt

def my_body(window):
    # -------------------------------- Titulo Zona Boton General --------------------------------
    tittle_1 = Label(window, text="Tablero de Control Principal",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_1.grid(row=3, column=0, columnspan=1)
    gntext.body_gncontrol_text(window)
    # -------------------------------- Botones de Encendido --------------------------------
    gnON.body_gncontrol_buttonON(window)
    # -------------------------------- Botonoes de Apagado --------------------------------
    gnOFF.body_gncontrol_buttonOFF(window)
    # -------------------------------- Titulo Zona Control Tiempos --------------------------------
    tittle_2 = Label(window, text=" Tiempo de Ejecucion ",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_2.grid(row=3, column=4, columnspan=5)
    tmbtn.body_control_time(window)
    # -------------------------------- Titulo Zona Muestra de tiempo transcurrido (OJO) --------------------------------
# boton de parada y start
    tittle_3 = Label(window, text=" Tiempo de Ejecucion " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_3.grid(row=3, column=7, columnspan=8)
    cnt.visible_count(window)
    # -------------------------------- Titulo Zona Alertas (Inferior) --------------------------------
#advertencia escrita delagua y conexiones de la maquina