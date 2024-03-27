from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import center as cin


fig, ax = plt.subplots(facecolor="#05FFBF")
plt.title("Grafica animada de Tkinter", color="#000000", size = 16, family= "Arial")

x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)

line, = ax.plot(x, y, color = "m", marker="o", linestyle="dotted", linewidth=5, 
                markersize=1, markeredgecolor="m")

def animate(i):
    x,xx,xxx,y,yy,yyy = cin.central()
    x = np.array(x)
    y = np.array(y)
    line.set_ydata(y)
    line.set_xdata(x)
    print(line)
    return line,

def iniciar():
    global ani
    ani = animation.FuncAnimation(fig, animate, interval = 20, blit=True, save_count=10)
    canvas.draw()

def pausar():
    ani.event_source.stop()

def reanudar():
    ani.event_source.start()

window = Tk()
window.geometry("1750x800")
window.wm_title("Grafica Animada de Tkinter ajua")

frame = Frame(window, bg="white", bd=3)
frame.pack(expand=1, fill="both")

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill="both")

Button(frame, text="Grafica Datos", width=15, bg="purple4", fg="white", command=iniciar).pack(pady=5, side="left", expand=1)
Button(frame, text="Pausar", width=15, bg="salmon", fg="white", command=pausar).pack(pady=5, side="left", expand=1)
Button(frame, text="Reaunar", width=15, bg="red", fg="white", command=reanudar).pack(pady=5, side="left", expand=1)

window.mainloop()

# window = Tk()
# window.geometry("1750x800")
# window.wm_title("Grafica Matplotlib")
# #window.minsize(width=1600, height=300)
# window.title("Graficas de Sensores(by: RuisoArt)")

# # intento 9000 a ver si sale esta pingada
# mpl.rcParams.update(mpl.rcParamsDefault)
# plt.style.use("ggplot")

# while True:
#         frame = Frame(window)#, bg="#FFFFFF")
#         frame.grid(row=0, column=0, sticky="nsew")

#         x,xx,xxx,y,yy,yyy = cin.central()

#         x = np.array(x)
#         y = np.array(y)

#         xx = np.array(xx)
#         yy = np.array(yy)

#         xxx = np.array(xxx)
#         yyy = np.array(yyy)

#         #fig, ax = plt.subplots(1, 3, dpi=80, figsize=(13,4), sharey=True, facecolor="#00FF00" )
#         fig, ax = plt.subplots(3, 1, dpi=80, figsize=(22,10), sharey=True, facecolor="#FFFFFF" )
#         fig.suptitle("Historial de Registro de Sensores - Maquina de Niebla Salina\n"
#                         "Vizualizacion de datos en Tiempo Real")

#         ax[0].plot(x, y, color='r') #x,y,color
#         ax[0].set_title("SENSOR "+"1"+" DS18B20")
#         ax[0].set_ylabel("Temperatura (°C)")
#         #ax[0].set_xlabel("Tiempo (h)")

#         ax[1].plot(xx, yy, color='g')
#         ax[1].set_title("SENSOR "+"2"+" DS18B20")
#         ax[1].set_ylabel("Temperatura (°C)")
#         #ax[1].set_xlabel("Tiempo (h)")

#         ax[2].plot(xxx, yyy, color='b')
#         ax[2].set_title("SENSOR "+"3"+" LM35")
#         ax[2].set_ylabel("Temperatur (°C)")
#         ax[2].set_xlabel("Tiempo (h)")

#         canvas = FigureCanvasTkAgg(fig, master=frame) #esto crea el area de dibujo en tkinter
#         canvas.draw()
#         canvas.get_tk_widget().grid(row=1, column=0, rowspan=3)

#         window.mainloop()



# #