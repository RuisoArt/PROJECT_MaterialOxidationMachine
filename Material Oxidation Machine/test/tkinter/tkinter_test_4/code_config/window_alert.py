from tkinter import *

def my_alert_window():
    alert = Tk()
    alert.title("Alert")
    alert.geometry("1000x1000")

    tittle = Label (alert, text=
                            +"       mmmWWWWWWWmmm       \n"
                            +"    mWWWWWWWWWWWWWWWWWm    \n"
                            +"   -WWWWWWWWWWWWWWWWWWW-   \n"
                            +"  m-WWWWWWWWWWWWWWWWWWW-     SE HA INGRESADO UNA VARIABLE\n"
                            +"  W--WWWWWWWWWWWWWWWWW--W    DIFERENTE A UN NUMERO ENTERO \n"
                            +"  WW--WWWWWWWWWWWWWWW--WW    O FLOTANTE, PARA EL INICIO DEL\n"
                            +"  WW--     WWWWW     --WW    TIEMPO DE EJECUCION DEL PROGRAMA.\n"
                            +"  mW        WWW       -Wm  \n"
                            +"   W-      WW WW      -W   \n"
                            +"  m--WWWWWWW   WWWWWWW--m    POR FAVOR INGRESE UN NUMERO Y NO\n"
                            +"   WWW    WW   WW    WWWm    UN CARACTER DIFERENTE POR TECLADO\n"
                            +"     W    WWWWWWW    Ww    \n"
                            +"     WW  ---------  WW     \n"
                            +"     WWW --------- WWW     \n"
                            +"      WWW--------WWW      \n"
                            +"        WWWWWWWWWWW        \n"
                            +"          WWWWWWW          \n"
                     ,bg="#FF0000", font="Helvetica 15", fg="white")
    tittle.grid(row=0, column=0)
    #tittle.pack(fill=X)
    alert.mainloop()