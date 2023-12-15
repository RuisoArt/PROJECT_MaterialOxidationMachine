from tkinter import *
import tkinter as tk

from code_body import general_control_text as gntext
from code_body import general_control_ON as gnON
from code_body import general_control_OFF as gnOFF

def my_body(window):
    # -------------------------------- Titulo Zona Boton General --------------------------------
    tittle_1 = Label(window, text="Tablero de Control Principal",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_1.grid(row=3, column=0, columnspan=1)
    # -------------------------------- Titulos de Controles --------------------------------
    gntext.body_gncontrol_text(window)
    # -------------------------------- Botones de Encendido --------------------------------
    gnON.body_gncontrol_buttonON(window)
    # -------------------------------- Botonoes de Apagado --------------------------------
    gnOFF.body_gncontrol_buttonOFF(window)
    # -------------------------------- Titulo Zona Control Tiempos --------------------------------
    tittle_2 = Label(window, text=" Tiempo de Ejecucion ",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    tittle_2.grid(row=3, column=4, columnspan=5)

    parraf = Label(window
                   ,text=" "
                        +"Lorem ipsum dolor sit amet, \n" 
                        +"consectetur adipiscing elit, \n"
                        +"sed do eiusmod tempor incididunt \n"
                        +"ut labore et dolore magna aliqua. \n"
                        +"Ut enim ad minim veniam, quis \n"
                        +"nostrud exercitation ullamco \n"
                        +"laboris nisi ut aliquip ex ea \n"
                        +"commodo consequat."
                        +" "
                   ,bg="#212F3D", font="Helvetica 12", fg="#FFFFFF")
    parraf.grid(row=4, rowspan=5, column=4, columnspan=5)

    Time_text = Label(window, text="Time (min): ", font="Helvetica 12")
    Time_var = Entry(window, font="Helvetica 13", width=10, justify="center")

    Time_text.grid(row=8, column=4)
    Time_var.grid(row=8, column=5, padx=1)

#OJO no estan aun programados para hacer una accion real de encedidos de la CLI ni para ejecutar el temporizador que terminara larutina con el apagado en cLI
    
    # -------------------------------- Titulo Zona Muestra de tiempo transcurrido (OJO) --------------------------------
# boton de parada y start
    # -------------------------------- Titulo Zona Alertas (Inferior) --------------------------------
#advertencia escrita delagua y conexiones de la maquina