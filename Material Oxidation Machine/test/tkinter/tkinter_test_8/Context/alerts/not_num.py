from tkinter import *

def alert_not_number():
    alert = Tk()
    alert.title("La entrada no es un numero")
    alert.geometry("530x180")

    title = Label(alert, text="🚫 ENTRADA NO VALIDA\nSE INGRESO ALGO \nDIFERENTE A UN NUMERO \nINTENTE NUEVAMENTE"
                  ,bg="#1F618D", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

alert_not_number()