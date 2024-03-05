from tkinter import *
import tkinter as tk
import datetime as dt
import time

from code_gpio import output_7_seven as out7
from code_body import count_control as my_count

def notices_body_control(window):

    tittle_3 = Label(window, text=" Mensajes del Proceso " ,bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2, width=20)
    tittle_3.grid(row=3, column=8, columnspan=10)

    date = dt.datetime.now()

    join = Label(window, text="Software iniciado en: \n\n"
                                +"Fecha: \n"
                                +str(date.strftime("%A %B %Y")) +"\n"
                                +str(date.strftime("%x")) +"\n\n"
                                +"Hora: \n"
                                +str(date.strftime("%X"))
                        ,bg="#82E0AA", font="Helvetica 12", fg="#000000")
    join.grid(row=4, rowspan=5 ,column=8, columnspan=10)

def button_start(window, number, segundos):
    date = dt.datetime.now()
    if number:
        join = Label(window, text="Se ha iniciado el proceso \n Boton START\n"
                                +"Hora: "+str(date.strftime("%X"))+"\n"
                                +"Trabajo estipulado para durar: "+str(number)+" min\n"
                                +"Esto equivale a: "+str(segundos)+" s"
                        ,bg="#F39C12", font="Helvetica 12", fg="#000000")
        join.grid(row=8, rowspan=10 ,column=8, columnspan=10)
        
        restante = segundos
        my_count.window_reverse_count(window, number, segundos, restante)
        while True:
            if restante >0:
                restante= restante - 1
                my_count.window_reverse_count(window, number, segundos, restante)
                time.sleep(1)
            else:
                my_count.finished_window(window)
                out7.output_off(7)
                print("finised!")
                break


    else:
        join = Label(window, text="No se recibio nada"
                        ,bg="#F39C12", font="Helvetica 12", fg="#000000")
        join.grid(row=8, rowspan=10 ,column=8, columnspan=10)

def button_stop(window, call):
    out7.output_off(7)
    date = dt.datetime.now()
    if call == "now":
        join = Label(window, text="Se ha parado el proceso \n Boton STOP\n"
                                +"Hora: "+str(date.strftime("%X"))                                
                        ,bg="#EC7063", font="Helvetica 12", fg="#000000")
        join.grid(row=14, rowspan=16 ,column=8, columnspan=10)
    else:
        join = Label(window, text="No se recibio nada"
                        ,bg="#EC7063", font="Helvetica 12", fg="#000000")
        join.grid(row=14, rowspan=16 ,column=8, columnspan=10)