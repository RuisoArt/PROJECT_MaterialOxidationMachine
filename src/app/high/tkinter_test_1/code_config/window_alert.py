from tkinter import *

def my_alert_window():
    alert = Tk()
    alert.title("Alert")
    alert.geometry("1000x1000")

    tittle = Label (alert, text=
                            +"       mmmWWWWWWWmmm       \n"
                            +"    mWWWWWWWWWWWWWWWWWm    \n"
                            +"   │░░░░░░░░░░░░░░░░░░░│   \n"
                            +"  ▌│░░░░░░░░░░░░░░░░░░░│     SE HA INGRESADO UNA VARIABLE\n"
                            +"  ░└┐░░░░░░░░░░░░░░░░░┌┘░    DIFERENTE A UN NUMERO ENTERO \n"
                            +"  ░░└┐░░░░░░░░░░░░░░░┌┘░░    O FLOTANTE, PARA EL INICIO DEL\n"
                            +"  ░░┌┘     ░░░░░     └┐░░    TIEMPO DE EJECUCION DEL PROGRAMA.\n"
                            +"  ▌░        ░░░       │░▐  \n"
                            +"   ░│      ░░ ░░      │░   \n"
                            +"  ▀─┘░░░░░░░   ░░░░░░░└─▀    POR FAVOR INGRESE UN NUMERO Y NO\n"
                            +"   WWW    ░░   ░░    ░░░▄    UN CARACTER DIFERENTE POR TECLADO\n"
                            +"     W    ░░░░░░░    Ww    \n"
                            +"     WW  ─┬┬┬┬┬┬┬─  WW     \n"
                            +"     WWW ┬┼┼┼┼┼┼┼┬ WWW     \n"
                            +"      WWW└┴┴┴┴┴┴┴┘WWW      \n"
                            +"        WWWWWWWWWWW        \n"
                            +"          WWWWWWW          \n"
                     ,bg="#FF0000", font="Helvetica 15", fg="white")
    tittle.grid(row=0, column=0)
    #tittle.pack(fill=X)
    alert.mainloop()