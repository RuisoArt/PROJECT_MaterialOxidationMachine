from tkinter import *

def alert_out_of_range_month():
    alert = Tk()
    alert.title("Numero Fuera de rango")
    alert.geometry("469x144")

    title = Label(alert, text="❌ NUMERO DEL MES\nFUERA DE RANGO\nINTENTA NUEVAMENTE"
                  ,bg="#E74C3C", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

def alert_out_of_range_day():
    alert = Tk()
    alert.title("Numero Fuera de rango")
    alert.geometry("469x144")

    title = Label(alert, text="❌ NUMERO DEL DIA\nFUERA DE RANGO\nINTENTA NUEVAMENTE"
                  ,bg="#E74C3C", font="Helvetica 30", fg="white",)
    title.grid(row=0, column=0)

    alert.mainloop()

def alert_out_of_hour():
    alert = Tk()
    alert.title("Rango de hora equivocado")
    alert.geometry("480x190")

    title = Label(alert, text="❌\nRANGO DE HORAS\nINGRESADO NO VALIDO\nINTENTA NUEVAMENTE"
                  ,bg="#E74C3C", font="Helvetica 30", fg="white", justify="center")
    title.grid(row=0, column=0)

    alert.mainloop()

alert_out_of_hour()