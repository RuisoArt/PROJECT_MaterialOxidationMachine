from tkinter import *
import tkinter as tk

from code_body import minute_control as mint
from code_body import notices_control as ntc

def body_control_time(window):
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
    btn_start = Button(window, text=" START ", font="Helvetica 12", bg="#2ECC71", fg="white", width="20",
                       command= lambda: mint.get_my_variables(window, Time_var)) 
    btn_stop  = Button(window, text=" STOP ",  font="Helvetica 12", bg="#FF0055", fg="white", width="20",
                       command= lambda: ntc.button_stop(window, "now") )

    btn_start.grid(row=9,  column=4, columnspan=5)
    btn_stop.grid (row=10, column=4, columnspan=5)


    