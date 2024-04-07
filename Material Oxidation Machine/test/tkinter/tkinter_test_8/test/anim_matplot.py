import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import datetime

import threading

def read_doc(): 
    """
        Se puede leerel archivo en tiempo real o irmirando el puerto serial 
    """
    route = "loot/"
    day = 22
    month = "March"
    year = 2024
    mensaje = str(day)+"_"+str(month)+"_"+str(year)
    dataset_name = "doc_MaterialOxidationMachine_"+mensaje+".txt"
    df_sensors = pd.read_csv(route+dataset_name, sep=" ")
    print(df_sensors.head(3))

    return df_sensors

def create_arrays(df_sensors):
    #trabajo sabiendo que son la misma cantidad de datos en las tres columnas
    total_data = int(df_sensors.count()[0])
    print("tota de datos: "+str(total_data))
    ar_temp1, ar_temp2, ar_temp3 = [], [], []
    for i in range(0, total_data):
        ar_temp1.append(df_sensors.loc[:,'temp1'][i])
        ar_temp2.append(df_sensors.loc[:,'temp2'][i])
        ar_temp3.append(df_sensors.loc[:,'temp3'][i])
    print(ar_temp1)
    print(ar_temp2)
    print(ar_temp3)

    return ar_temp1, ar_temp2, ar_temp3

def create_axis(ar_temp1, ar_temp2, ar_temp3):
    y = np.array(ar_temp1)
    yy = np.array(ar_temp2)
    yyy = np.array(ar_temp3)

    return y, yy, yyy



# gData = []
# gData.append([0.0])
# gData.append([0.0])

# def getData():
#     while True:
#         # leer el documento de loot --------------------------------------------------------
#         df_sensors = read_doc()
#         #ahora crear los array secada bicho--------------------------------------------------    
#         #total_data , ar_hour, ar_temp1, ar_temp2, ar_temp3 = create_arrays(df_sensors)
#         ar_temp1 = create_arrays(df_sensors)   
#         # graficarlos --------------------------------------------------------------------------
#         return ar_temp1

# dataCollector = threading.Thread(target=getData, args=(gData))
# dataCollector.start()

# def update_line(actual_frame, hl, ar_temp1):
#     dx = np.array(range(len(ar_temp1[1])))
#     dy = np.array(ar_temp1[1])
#     # obtener los valores de x y y respectivamente ----------------------------------------
#     #x, y, yy, yyy = create_axis(ar_hour, ar_temp1, ar_temp2, ar_temp3)
#     # -------------------------------- de la nimacion setiar los datos de x y y --------------------------------
#     hl.set_data(dx, dy)
#     return hl


# window = Tk()
# window.geometry("1750x800")
# window.wm_title("Grafica Matplotlib")
# window.title("Graficas de Sensores(by: RuisoArt)")

# frame = Frame(window)#, bg="#FFFFFF")
# frame.grid(row=0, column=0, sticky="nsew")

"""
    aqui iria la árte de obtener los valores respectivos de x y y respectivamente
"""

mpl.rcParams.update(mpl.rcParamsDefault)
plt.style.use("ggplot")

x_data = []
y_data = []

fig = plt.figure()
#fig, ax = plt.subplots(dpi=80, figsize=(22,10), sharey=True, facecolor="#FFFFFF" )
#fig, ax = plt.subplots(3, 1, dpi=80, figsize=(22,10), sharey=True, facecolor="#FFFFFF" )
fig.suptitle("Historial de Registro de Sensores de Temperatura - Maquina de Niebla Salina\n"
                "Grafica en tiempo Real", fontsize=20)

line, = plt.plot_date(x_data, y_data, '-')
#plt.plot(gData[0], gData[1], color='r') #x,y,color
#plt.title("SENSOR 1 DS18B20")
#plt.ylabel("Temperatura (°C)")
#plt.xlabel("Tiempo (h)")

def grafica():
    x_data.append(datetime.now())
    df_sensors = read_doc()
    ar_temp1, ar_temp2, ar_temp3 = create_arrays(df_sensors)
    y, yy, yyy = create_axis( ar_temp1, ar_temp2, ar_temp3)
    y_data.append(y)

    line.set_data(x_data, y_data)
    fig.gca().relim()
    fig.gca().autoscale_view()
    return line,

animacion = FuncAnimation(fig, grafica, interval=1000)

# ax[1].plot(x, yy, color='g')
# ax[1].set_title("SENSOR 2 DS18B20")
# ax[1].set_ylabel("Temperatura (°C)")

# ax[2].plot(x, yyy, color='b')
# ax[2].set_title("SENSOR 3 LM35")
# ax[2].set_ylabel("Temperatura (°C)")
# ax[2].set_xlabel("Tiempo (h)")

#line_anim = animation.FuncAnimation(fig, update_line, fargs=(hl, gData), interval=50, blit= False)

#canvas = FigureCanvasTkAgg(fig, master=frame) #esto crea el area de dibujo en tkinter
#canvas.draw()
#canvas.get_tk_widget().grid(row=1, column=0, rowspan=3)

#window.mainloop()
plt.show()
