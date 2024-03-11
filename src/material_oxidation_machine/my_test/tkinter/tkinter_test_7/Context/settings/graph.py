import pandas as pd
import numpy as np
import seaborn as sns

from tkinter import Tk, Frame, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def my_grah(window, my_minh, my_maxh, df_sensors):
    print("llegaste a graficar")
    init = int(my_minh) * 10000
    finish = int(my_maxh) * 10000

    print(df_sensors.keys())

    df_temp     = pd.DataFrame(df_sensors.loc[:, ['hora','temp1']])
    df_temp_2   = pd.DataFrame(df_sensors.loc[:, ['hora','temp2']])
    df_temp_3   = pd.DataFrame(df_sensors.loc[:, ['hora','temp3']])

    # sensor teperatura 1
    array_temp , array_hour = [], []
    max_values_temp = df_temp.count()[1]   
    # SENSOR 1
    array_temp , array_hour = section_array(init, finish, df_temp, max_values_temp, array_temp , array_hour, 'temp1')
    section_plot(array_temp , array_hour, my_minh, my_maxh, '1')
    
    # sensor teperatura 2
    array_temp , array_hour = [], []
    max_values_temp = df_temp_2.count()[1]
    # SENSOR 2
    array_temp , array_hour = section_array(init, finish, df_temp_2, max_values_temp, array_temp , array_hour, 'temp2')
    section_plot(array_temp , array_hour, my_minh, my_maxh, '2')

    # sensor teperatura 3
    array_temp , array_hour = [], []
    max_values_temp = df_temp_3.count()[1]
    # SENSOR 3
    array_temp , array_hour = section_array(init, finish, df_temp_3, max_values_temp, array_temp , array_hour, 'temp3')
    section_plot(array_temp , array_hour, my_minh, my_maxh, '3')
    

def section_array(init, finish, df_data, max_values_temp, array_temp , array_hour, valor):

    for i in range(0, max_values_temp):
        if df_data.loc[:,'hora'][i] >= init and df_data.loc[:,'hora'][i] <= (init+10999): 
            array_temp.append(df_data.loc[:, valor][i])
            array_hour.append(df_data.loc[:,'hora'][i])

        elif df_data.loc[:,'hora'][i] >= finish and df_data.loc[:,'hora'][i] <= (finish+10999):
            array_temp.append(df_data.loc[:, valor][i])
            array_hour.append(df_data.loc[:,'hora'][i])

    print("termino la seccion de arrays")
    print(array_temp)
    print(array_hour)
    return array_temp , array_hour
    
def section_plot(array_temp , array_hour, init_hour, finish_hour,valor):
    print("llego a plot")
    print(array_temp)
    print(array_hour)

    window = Tk()
    window.geometry("1200x700")
    window.wm_title("Grafica Matplotlib")
    window.minsize(width=1200, height=700)

    frame = Frame(window, bg="#FFFFFF")
    frame.grid(row=0, column=0, sticky="nsew")

    # nombres = ["Azul", "Rojo", "Verde", "Magenta", "Negro"]
    # colores = ["blue", "red", "green", "magenta", "black"]
    # tamaño = [15, 25, 10, 20, 30]

    x = np.array(array_hour)
    y = np.array(array_temp)

    fig, ax = plt.subplots(dpi=80, figsize=(15,8), sharey=True, facecolor="#E5E7E9" )
    fig.suptitle("Historial de Registro de Temperatura SENSOR "+valor+"\n"+
                 "Hora Inicio: "+str(init_hour)+":00:00"
                 " Hora Final: "+str(finish_hour)+":59:59")
    fig.align_xlabels("Tiempo (h)")
    fig.align_ylabels("Temperatura °C")
    ax.plot(x, y, color='r', marker="o", markersize=0, linewidth=2)

    canvas = FigureCanvasTkAgg(fig, master=frame) #esto crea el area de dibujo en tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=3)

    print("termino plotting")
    window.mainloop()
