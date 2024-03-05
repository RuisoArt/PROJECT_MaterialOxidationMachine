from tkinter import *
from settings import result

def alert_confirmfile(window, df_sensors, mensaje):
    alert = Tk()
    alert.title("Archivo encontrado")
    alert.geometry("550x97")

    title = Label(alert, text="✅ ARCHIVO ENCONTRADO\nPUEDE CONTINUAR"
                  ,bg="#2ECC71", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    result.show_generaldata_ofDataframe(window, df_sensors, mensaje)

    alert.mainloop()

#alert_confirmfile()