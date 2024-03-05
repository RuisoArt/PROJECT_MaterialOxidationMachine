from tkinter import *
import tkinter as tk

import datetime as dt

from code_body import general_control_text as gntext
from code_body import general_control_ON as gnON
from code_body import general_control_OFF as gnOFF
from code_body import time_control as tmbtn
from code_config import count as cnt
from code_body import notices_control as ntc

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
    ntc.notices_body_control(window)
    
    
    #cnt.visible_count(window)
    # -------------------------------- Titulo Zona Alertas (Inferior) --------------------------------
#advertencia escrita delagua y conexiones de la maquina