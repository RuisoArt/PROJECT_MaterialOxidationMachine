from datetime import datetime
import tkinter as tk

var_refreshTime = 500  # En milisegundos
time_init= datetime.now()

def the_time(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas*60*60
    minutos = int(segundos/60)
    segundos -= minutos*60

    my_time = f"[GT]: {horas:02d}:{minutos:02d}:{segundos:02d}"
    print("Tiempo: ", my_time)
    #get_my_time(my_time)
    return my_time

"""def get_my_time(my_time):
    the_time = str(my_time)
    return the_time"""

def get_format_time():
    segundos_transcurridos = (datetime.now() - time_init).total_seconds()
    return the_time(int(segundos_transcurridos))

def refresh_time():
    current_time.set(get_format_time())
    raiz.after(var_refreshTime, refresh_time)


raiz = tk.Tk()
current_time = tk.StringVar(raiz, value=get_format_time())
raiz.etiqueta = tk.Label(raiz, textvariable=current_time, font=f"Consolas 65")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Cronometro Tiempo Transcurrido General del equipo [General Time]")
refresh_time()
app.pack()
app.mainloop()

