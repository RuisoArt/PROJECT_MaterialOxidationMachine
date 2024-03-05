from tkinter import *
import tkinter as tk

import datetime as dt

from code_body import general_control_text as gntext
from code_body import general_control_ON as gnON
from code_body import general_control_OFF as gnOFF
from code_body import time_control as tmbtn
from code_config import count as cnt

def my_body(window):
    # -------------------------------- Titulo Zona Boton General --------------------------------
    gntext.body_gncontrol_text(window)
    # -------------------------------- Botones de Encendido --------------------------------
    gnON.body_gncontrol_buttonON(window)
    # -------------------------------- Botonoes de Apagado --------------------------------
    gnOFF.body_gncontrol_buttonOFF(window)
    # -------------------------------- Titulo Zona Control Tiempos --------------------------------
    tmbtn.body_control_time(window)
    # -------------------------------- Titulo Zona Muestra de tiempo transcurrido (OJO) --------------------------------
# boton de parada y start
    tittle_3 = Label(window, text=" Avisos " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2, width=20)
    tittle_3.grid(row=3, column=8, columnspan=9)

    date = dt.datetime.now()

    join = Label(window, text="Software iniciado en: \n\n"
                                +"Fecha: \n"
                                +str(date.strftime("%A %B %Y")) +"\n"
                                +str(date.strftime("%x")) +"\n\n"
                                +"Hora: \n"
                                +str(date.strftime("%X"))
                        ,bg="#82E0AA", font="Helvetica 12", fg="#000000")
    join.grid(row=4, rowspan=5 ,column=8, columnspan=9)
    
    
    #cnt.visible_count(window)
    # -------------------------------- Titulo Zona Alertas (Inferior) --------------------------------
#advertencia escrita delagua y conexiones de la maquina