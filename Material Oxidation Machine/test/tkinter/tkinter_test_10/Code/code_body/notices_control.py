from tkinter import *
import tkinter as tk
import datetime as dt
import time

from code_gpio import output_7_seven as out7
from code_body import count_control as my_count
from code_config import in_process as oin

def notices_body_control(window):
    date = dt.datetime.now()
    
    tittle_3 = Label(window, text=" Mensajes del Proceso " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2, width=20)
    
    join = Label(window, text="Software iniciado en: \n\n"
                                +"Fecha: \n"
                                +str(date.strftime("%A %B %Y")) +"\n"
                                +str(date.strftime("%x")) +"\n\n"
                                +"Hora: \n"
                                +str(date.strftime("%X"))
                        ,bg="#F39C12", font="Helvetica 12", fg="#000000")

    tittle_3.grid(row=3, column=10, columnspan=12)
    join.grid(row=4, rowspan=5 ,column=10, columnspan=12)

def button_start(window, rrh_var, rrm_var):
    date = dt.datetime.now()

    hora = int(rrh_var)
    minute = int(rrm_var)

    if hora and minute:
        join = Label(window, text="Se ha iniciado el proceso \n Boton START\n"
                                +"Hora: "+str(date.strftime("%X"))+"\n"
                                +"Trabajo estipulado para durar hasta las:\n"
                                +str(hora)+":"+str(minute)
                                #Se podria restar la hora actual de la ingresa y tambien con minutos para saber cuanto tiempo es de ejcucion
                        ,bg="#82E0AA", font="Helvetica 12", fg="#000000")
        join.grid(row=7, rowspan=8 ,column=10, columnspan=12)

        oin.machine_on(window, hora, minute)

    else:
        join = Label(window, text="No se recibio nada"
                        ,bg="#F39C12", font="Helvetica 12", fg="#000000")
        join.grid(row=7, rowspan=8 ,column=10, columnspan=12)


def finich_process(window, call):
    out7.output_off(7)
    date = dt.datetime.now()
    if call == "now":
        join = Label(window, text="Se ha parado el proceso \n Boton STOP\n"
                                +"Hora: "+str(date.strftime("%X"))                                
                        ,bg="#EC7063", font="Helvetica 12", fg="#000000")
        join.grid(row=10, rowspan=11 ,column=10, columnspan=12)
    else:
        join = Label(window, text="No se recibio nada"
                        ,bg="#EC7063", font="Helvetica 12", fg="#000000")
        join.grid(row=10, rowspan=11 ,column=10, columnspan=12)