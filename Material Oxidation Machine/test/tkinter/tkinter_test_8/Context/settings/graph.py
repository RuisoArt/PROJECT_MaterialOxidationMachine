import pandas as pd
import numpy as np
import seaborn as sns

#from tkinter import Tk, Frame, Button
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as mpl

def my_grah(window, my_minh, my_maxh, df_sensors):
    print("llegaste a graficar")
    init = int(my_minh) * 10000
    finish = int(my_maxh) * 10000

    print(df_sensors.keys())

    df_temp     = pd.DataFrame(df_sensors.loc[:, ['hora','temp1']])
    df_temp_2   = pd.DataFrame(df_sensors.loc[:, ['hora','temp2']])
    df_temp_3   = pd.DataFrame(df_sensors.loc[:, ['hora','temp3']])

    #los tres sensores mother foca
    # SENSOR 1
    array_temp1 , array_hour1 = [], []
    max_values_temp1 = df_temp.count()[1]
    array_temp1 , array_hour1 = section_array(init, finish, df_temp, max_values_temp1, array_temp1 , array_hour1, 'temp1')
    # SENSOR 2
    array_temp2 , array_hour2 = [], []
    max_values_temp2 = df_temp_2.count()[1]
    array_temp2 , array_hour2 = section_array(init, finish, df_temp_2, max_values_temp2, array_temp2 , array_hour2, 'temp2')
    # SENSOR 3
    array_temp3 , array_hour3 = [], []
    max_values_temp3 = df_temp_3.count()[1]
    array_temp3 , array_hour3 = section_array(init, finish, df_temp_3, max_values_temp3, array_temp3 , array_hour3, 'temp3')

    section_plot(array_temp1 , array_hour1, my_minh, my_maxh, '1',
                 array_temp2 , array_hour2, '2',
                 array_temp3 , array_hour3, '3')
    

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
    
#def section_plot(array_temp , array_hour, init_hour, finish_hour,valor):
def section_plot(array_temp1 , array_hour1, init_hour, finish_hour, valor1,
                 array_temp2 , array_hour2, valor2,
                 array_temp3 , array_hour3, valor3):    
    print("llego a plot")
    print(array_temp1)
    print(array_hour1)
    print(array_temp2)
    print(array_hour2)
    print(array_temp3)
    print(array_hour3)

    # intento 9000 a ver si sale esta pingada
    mpl.rcParams.update(mpl.rcParamsDefault)
    plt.style.use("ggplot")

    window = Tk()
    window.geometry("1750x800")
    window.wm_title("Grafica Matplotlib")
    #window.minsize(width=1600, height=300)
    window.title("Graficas de Sensores(by: RuisoArt)")
    
    frame = Frame(window)#, bg="#FFFFFF")
    frame.grid(row=0, column=0, sticky="nsew")

    x = np.array(array_hour1)
    y = np.array(array_temp1)

    xx = np.array(array_hour2)
    yy = np.array(array_temp2)

    xxx = np.array(array_hour3)
    yyy = np.array(array_temp3)

    #fig, ax = plt.subplots(1, 3, dpi=80, figsize=(13,4), sharey=True, facecolor="#00FF00" )
    fig, ax = plt.subplots(3, 1, dpi=80, figsize=(22,10), sharey=True, facecolor="#FFFFFF" )
    fig.suptitle("Historial de Registro de Sensores - Maquina de Niebla Salina\n"
                 "Hora Inicio: "+str(init_hour)+":00:00"
                 " Hora Final: "+str(finish_hour)+":59:59 \n\n\n\n", fontsize=20)
    
    
    ax[0].plot(x, y, color='r') #x,y,color
    ax[0].set_title("SENSOR "+valor1+" DS18B20")
    ax[0].set_ylabel("Temperatura (°C)")
    #ax[0].set_xlabel("Tiempo (h)")

    ax[1].plot(xx, yy, color='g')
    ax[1].set_title("SENSOR "+valor2+" DS18B20")
    ax[1].set_ylabel("Temperatura (°C)")
    #ax[1].set_xlabel("Tiempo (h)")

    ax[2].plot(xxx, yyy, color='b')
    ax[2].set_title("SENSOR "+valor3+" LM35")
    ax[2].set_ylabel("Temperatura (°C)")
    ax[2].set_xlabel("Tiempo (h)")
    
    canvas = FigureCanvasTkAgg(fig, master=frame) #esto crea el area de dibujo en tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, rowspan=3)

    window.mainloop()

    

    

       
