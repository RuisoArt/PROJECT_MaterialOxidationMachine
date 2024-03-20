from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import pull_data as pull
import split_dataframe as splt

dataframe = pull.pull_dataframe()

if len(dataframe.index) == 0:
        print("No hay archivo que utilizar")
else:
    print("tenemos dataframe")
    df_temp1, df_temp2, df_temp3 = splt.split_info(dataframe)
    #return df_sensors




# fig, ax = plt.subplots(facecolor="#05FFBF")
# plt.title("Grafica animada de Tkinter", color="#000000", size = 16, family= "Arial")

# x = np.arange(0, 4*np.pi, 0.01)
# y = np.sin(x)
# line, = ax.plot(x, y, color = "m", marker="o", linestyle="dotted", linewidth=5, 
#                 markersize=1, markeredgecolor="m")

# def animate(i):
#     line.set_ydata(np.sin(x+i/40))
#     print(line)
#     return line,

# def iniciar():
#     global ani
#     ani = animation.FuncAnimation(fig, animate, interval = 20, blit=True, save_count=10)
#     canvas.draw()

# def pausar():
#     ani.event_source.stop()

# def reanudar():
#     ani.event_source.start()

# window = Tk()
# window.geometry("642x535")
# window.wm_title("Grafica Animada de Tkinter ajua")

# frame = Frame(window, bg="white", bd=3)
# frame.pack(expand=1, fill="both")

# canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill="both")

# Button(frame, text="Grafica Datos", width=15, bg="purple4", fg="white", command=iniciar).pack(pady=5, side="left", expand=1)
# Button(frame, text="Pausar", width=15, bg="salmon", fg="white", command=pausar).pack(pady=5, side="left", expand=1)
# Button(frame, text="Reaunar", width=15, bg="red", fg="white", command=reanudar).pack(pady=5, side="left", expand=1)

# window.mainloop()