from tkinter import *

def alert_verify():
    alert = Tk()
    alert.title("Entrada verificada")
    alert.geometry("510x97")

    title = Label(alert, text="✅ ENTRADA VERIFICADA\nPUEDE CONTINUAR"
                  ,bg="#2ECC71", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

#alert_verify()