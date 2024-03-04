from tkinter import *
import tkinter as tk

def dataset_info(window, titulo, quantity, hourmin, hourmax,
                 temp1min, temp1max, temp1media, temp1mediana,
                 temp2min, temp2max, temp2media, temp2mediana,
                 temp3min, temp3max, temp3media, temp3mediana,
                 lv_total_0, lv_total_1, lv_suma):
        
    tittle          = Label(window, text="¡Registro Encontrado!",bg="#F4D03F", font="Helvetica 12", fg="#000000", height=2)
    subtittle       = Label(window, text="Nombre del Archivo: "+str(titulo),bg="#FFFFFF", font="Helvetica 10", fg="#000000", height=2)
    
    mensaje_cantidad = str( "Total Datos: "+quantity)
    mensaje_cantidad = mensaje_cantidad.replace('hora', '')
    mensaje_cantidad = mensaje_cantidad.replace('dtype: int64', '')
    txt_quantity    = Label(window, text=mensaje_cantidad, font="Helvetica 12", fg="#000000", height=2)

    mensaje_hora = str("Min: "+hourmin+"  Max: "+hourmax)
    mensaje_hora = mensaje_hora.replace('hora', '')
    mensaje_hora = mensaje_hora.replace('dtype: int64', '')
    mensaje_hora = mensaje_hora.replace('\n', '')
    txt_hour    = Label(window, text="Horarrio Registrado en el archivo: (HH:MM:SS)\n"+mensaje_hora, font="Helvetica 12", fg="#000000", height=2)   
        
    mensaje_temp1 = str("Min:"+temp1min +"  Max:"+ temp1max + "  Media:"+ temp1media + "  Mediana:"+ temp1mediana)
    mensaje_temp1 = mensaje_temp1.replace('temp1', '')
    mensaje_temp1 = mensaje_temp1.replace('dtype: int64', '')
    mensaje_temp1 = mensaje_temp1.replace('dtype: float64', '')
    mensaje_temp1 = mensaje_temp1.replace('\n', '')
    txt_tmp1     = Label(window, text="Temperatura (°C) SENSOR 1: \n"+str(mensaje_temp1), font="Helvetica 12", fg="#000000", height=3)
    

    mensaje_temp2 = str("Min:"+temp2min +"  Max:"+ temp2max + "  Media:"+ temp2media + "  Mediana:"+ temp2mediana)
    mensaje_temp2 = mensaje_temp2.replace('temp2', '')
    mensaje_temp2 = mensaje_temp2.replace('dtype: int64', '')
    mensaje_temp2 = mensaje_temp2.replace('dtype: float64', '')
    mensaje_temp2 = mensaje_temp2.replace('\n', '')
    txt_tmp2     = Label(window, text="Temperatura (°C) SENSOR 2: \n"+str(mensaje_temp2), font="Helvetica 12", fg="#000000", height=3)

    mensaje_temp3 = str("Min:"+temp3min +"  Max:"+ temp3max + "  Media:"+ temp3media + "  Mediana:"+ temp3mediana)
    mensaje_temp3 = mensaje_temp3.replace('temp3', '')
    mensaje_temp3 = mensaje_temp3.replace('dtype: int64', '')
    mensaje_temp3 = mensaje_temp3.replace('dtype: float64', '')
    mensaje_temp3 = mensaje_temp3.replace('\n', '')
    txt_tmp3     = Label(window, text="Temperatura (°C) SENSOR 3: \n"+str(mensaje_temp3), font="Helvetica 12", fg="#000000", height=3)

    mensaje_total0 = str("Porcentaje de Nivel Tanque Vacio ["
                        +str(lv_total_0)+"/"+str(lv_suma)+"]: "
                        +str(round( ((lv_total_0 * 100)/lv_suma) ,2)) +"%" )
    
    mensaje_total1 = str("Porcentaje de Nivel Tanque Lleno ["
                        +str(lv_total_1)+"/"+str(lv_suma)+"]: "
                        +str(round( ((lv_total_1 * 100)/lv_suma) ,2)) +"%" )
    
    txt_lv0 = Label(window, text=str(mensaje_total0), font="Helvetica 12", fg="#000000", height=3)
    txt_lv1 = Label(window, text=str(mensaje_total1), font="Helvetica 12", fg="#000000", height=3)

    tittle.grid       (row=3, column=10,  columnspan=18)
    subtittle.grid    (row=4, column=10,  columnspan=18)
    txt_quantity.grid (row=5, column=10,  columnspan=18)
    txt_hour.grid     (row=6, column=10,  columnspan=18)
    txt_tmp1.grid     (row=7, column=10,  columnspan=18)
    txt_tmp2.grid     (row=8, column=10,  columnspan=18)
    txt_tmp3.grid     (row=9, column=10,  columnspan=18)
    txt_lv0.grid      (row=10, column=10,  columnspan=18)
    txt_lv1.grid      (row=11, column=10,  columnspan=18)

