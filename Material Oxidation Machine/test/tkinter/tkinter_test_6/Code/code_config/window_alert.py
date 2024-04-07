from tkinter import *

def my_alert_window():
    alert = Tk()
    alert.title("Alert")
    alert.geometry("365x260") #ancho y alto

    tittle = Label (alert, text="⚠️\n"
                    +"SE HA INGRESADO UNA VARIABLE \n"
                    +"DIFERENTE A UN NUMERO ENTERO \n"
                    +"O BIEN UN FORMATO DE HORA QUE \n"
                    +"NO ES VALIDO PARA LA EJECUCION \n"
                    +"DEL PROGRAMA. "
                    +"\n\n"
                    +"RECUERDE SE DEBE INGRESAR EN \n"
                    +"FORMATO 24H Y LA HORA MAXIMA \n"
                    +"ES 23:53"
                    +"\n\n"
                    +"POR FAVOR VUELVA A INTENTARLO "
                    +"\n\n"
                   ,bg="#FF0000", font="Helvetica 15", fg="white", justify="left")
    tittle.grid(row=0, column=0)
    #tittle.pack(fill=X)
    alert.mainloop()

my_alert_window()

# ""
#                             +"       mmmWWWWWWWmmm                                             \n"
#                             +"    mWWWWWWWWWWWWWWWWWm                                          \n"
#                             +"   -WWWWWWWWWWWWWWWWWWW-                                         \n"
#                             +"  m-WWWWWWWWWWWWWWWWWWW-     SE HA INGRESADO UNA VARIABLE        \n"
#                             +"  W--WWWWWWWWWWWWWWWWW--W    DIFERENTE A UN NUMERO ENTERO        \n"
#                             +"  WW--WWWWWWWWWWWWWWW--WW    O FLOTANTE, PARA EL INICIO DEL      \n"
#                             +"  WW--     WWWWW     --WW    TIEMPO DE EJECUCION DEL PROGRAMA.   \n"
#                             +"  mW        WWW       -Wm                                        \n"
#                             +"   W-      WW WW      -W                                         \n"
#                             +"  m--WWWWWWW   WWWWWWW--m    POR FAVOR INGRESE UN NUMERO Y NO    \n"
#                             +"   WWW    WW   WW    WWWm    UN CARACTER DIFERENTE POR TECLADO   \n"
#                             +"     W    WWWWWWW    Ww                                          \n"
#                             +"     WW  ---------  WW                                           \n"
#                             +"     WWW --------- WWW                                           \n"
#                             +"      WWW--------WWW                                             \n"
#                             +"        WWWWWWWWWWW                                              \n"
#                             +"          WWWWWWW                                                \n"