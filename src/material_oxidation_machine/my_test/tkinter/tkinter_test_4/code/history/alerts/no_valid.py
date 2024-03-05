from tkinter import *

def alert_no_valid():
    alert = Tk()
    alert.title("No es valido")
    alert.geometry("489x97")

    title = Label(alert, text="⚠️ ENTRADA NO VALIDA\nINTENTA NUEVAMENTE"
                  ,bg="#FFC300", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

#alert_no_valid()