from tkinter import *
import tkinter as tk

from settings import file_name

def body_textzone_date(window):
        
    tittle = Label(window, text="Fecha del Registro",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    subtitle = Label(window, text="Recuerda solo escribir numeros en los siguientes recuadros!",bg="#FFFFFF", font="Helvetica 10", fg="#000000", height=2)
    
    text_1 = Label(window, text="El registro que quieres revisar de que AÑO es?:", font="Helvetica 12", fg="#000000", height=2)   
    input_year = Entry(window, font="Helvetica 14", width=10, justify="center")
    
    text_2 = Label(window, text="El registro que quieres revisar de que MES pertenece?:", font="Helvetica 12", fg="#000000", height=2)
    input_month = Entry(window, font="Helvetica 14", width=10, justify="center")
    text_3 = Label(window, text="Debes escribir el numero del mes que quieres revisar\ndel 1 al 12 segun corresponda.", font="Helvetica 12", fg="#000000", height=2, bg="#FFFFFF")
    text_4 = Label(window, text="\n[1] Enero [2] Febrero [3] Marzo [4] Abril\n"+
                                "[5] Mayo [6] Junio [7] Julio [8] Agosto\n"+
                                "[9] Septiembre [10] Octubre [11] Noviembre [12] Diciembre\n"
                                , font="Helvetica 12", fg="#000000", height=3, bg="#FFFFFF")

    text_5 = Label(window, text="El registro que quieres revisar de que DIA es?:", font="Helvetica 12", fg="#000000", height=2)
    input_day = Entry(window, font="Helvetica 14", width=10, justify="center")

    verify_variables = Button(window, text=" VERIFICAR DATOS ", font="Helvetica 12", bg="#2ECC71", fg="white", width="20",
                       command= lambda: file_name.my_file_name(input_year, input_month, input_day))

    tittle.grid          (row=3, column=0,  columnspan=8) #hasta columna 7
    subtitle.grid        (row=4, column=0,  columnspan=8) 
    text_1.grid          (row=5, column=0,  columnspan=8)
    input_year.grid      (row=6, column=0,  columnspan=8)
    text_2.grid          (row=7, column=0,  columnspan=8)
    input_month.grid     (row=8, column=0,  columnspan=8)
    text_3.grid          (row=9, column=0,  columnspan=8)
    text_4.grid          (row=10, column=0, columnspan=8)
    text_5.grid          (row=11, column=0, columnspan=8)
    input_day.grid       (row=12, column=0, columnspan=8)
    verify_variables.grid(row=13, column=0, columnspan=8)

    #funciones de las entradas tomadas para corroborar los registros


    #Boton de comprobar todo

    """
        
            
            
                
                
            
    """
