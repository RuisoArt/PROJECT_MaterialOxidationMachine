from tkinter import *
import tkinter as tk

from code_body import minute_control as mint
from code_body import notices_control as ntc

def body_control_time(window):
    tittle_2 = Label(window, text=" Tiempo de Ejecucion ",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    
    parraf = Label(window
                   ,text="A continuacion, debera ingresar el tiempo\n"
                        +"que quiere mantener encendida \n"
                        +"la Maquina de Niebla Salina.\n"
                        +"\n"
                        +"Debe ingresar la hora y los minutos\n"
                        +"en formato 24 horas (24h). La hora ingresada\n"
                        +"sera el momento en que la maquina se apague.\n"
                        +"Recuerde que el registro de los sensores se\n" 
                        +"da una vez se inicia el TABLERO PRINCIPAL\n"
                        +"y en caso de no haber suficiente agua en el \n"
                        +"tanque, la maquina se apagara sola sin \n" 
                        +"importar este proceso.\n"    
                   ,bg="#212F3D", font="Helvetica 12", fg="#FFFFFF")
    
    Time_text_hour = Label(window, text="Hora (24h): ", font="Helvetica 12")
    Time_text_min = Label(window, text="Minutos: ", font="Helvetica 12")

    hour_var = Entry(window, font="Helvetica 13", width=10, justify="center")
    min_var = Entry(window, font="Helvetica 13", width=10, justify="center")

    btn_start = Button(window, text=" START ", font="Helvetica 12", bg="#2ECC71", fg="white", width="20",
                        command= lambda: mint.get_my_variables(window, hour_var, min_var))



    tittle_2.grid                   (row=3,            column=4, columnspan=10)
    parraf.grid                     (row=4, rowspan=5, column=4, columnspan=10)
    Time_text_hour.grid             (row=9,            column=7)
    Time_text_min.grid              (row=10,           column=7)

    hour_var.grid(row=9, column=8)
    min_var.grid(row=10, column=8)

    btn_start.grid(row=11,  column=4, columnspan=10)

    #
    #Time_var = Entry(window, font="Helvetica 13", width=10, justify="center")

    

    


#OJO no estan aun programados para hacer una accion real de encedidos de la CLI ni para ejecutar el temporizador que terminara larutina con el apagado en cLI
    # 
    #btn_stop  = Button(window, text=" STOP ",  font="Helvetica 12", bg="#FF0055", fg="white", width="20",
    #                   command= lambda: ntc.button_stop(window, "now") )

    #
    #btn_stop.grid (row=10, column=4, columnspan=5)


    