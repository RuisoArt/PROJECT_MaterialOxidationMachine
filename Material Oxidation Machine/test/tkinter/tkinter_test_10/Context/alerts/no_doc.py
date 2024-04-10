from tkinter import *

def alert_no_document():
    alert = Tk()
    alert.title("Not Found")
    alert.geometry("630x97")

    title = Label(alert, text="📃 REGISTRO NO ENCONTRADO\nINTENTA NUEVAMENTE"
                  ,bg="#2980B9", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

#alert_no_document()