from tkinter import *
import tkinter as tk
import os
import header_p as h

# ---------------------------------------------------------------- Funciones extras
def control():
    print("Activado Control")

def registro():
    print("Activado Registro")

def reading():
    print("Activado Reading")

def emergency():
    print("Activado Button Emergency")

# ---------------------------------------------------------------- caracteristicas de la ventana
window = tk.Tk()
window.geometry("1170x900")
window.title("Material Oxidation Machine - Principal Window (by:RuisoArt)")
# ---------------------------------------------------------------- Logos desl sistema
img_rasplogo = PhotoImage(file= "./assets/img/COLOURRaspberryPI.png")
img_ustalogo = PhotoImage(file= "./assets/img/logo.png")

sm_img_rasp = img_rasplogo.subsample(5,5)
sm_img_usta = img_ustalogo.subsample(5,5)

img_rasp = Label(window, image = sm_img_rasp, width="100")
img_usta = Label(window, image = sm_img_usta, width="200")

img_rasp.grid(row=1, column=0)
img_usta.grid(row=1, column=19)
# ---------------------------------------------------------------- Seccion de header
h.my_header(window)
# ---------------------------------------------------------------- seccion de img
img_machine = PhotoImage(file= "./assets/img/machine.png")
sm_machine = img_machine.subsample(2,2)
machine = Label(window, image=sm_machine, width="1000")
machine.grid(row=3, column=0, columnspan=20)
#---------------------------------------------------------------- seccion de body
tittle = Label(window, text="Selecciona el Tablero o Software que deseas activar", font="Helvetica 15", fg="#000000", height=2)
tittle.grid(row=4, column=0,  columnspan=20)
#----------------------------------------------------------------
img_control = PhotoImage(file= "./assets/img/control.png")
sm_control = img_control.subsample(4,4)
controlpng = Label(window, image=sm_control, width="300")
controlpng.grid(row=5, column=0, columnspan=10)

BTN_control = Button(window, text=" TABLERO DE CONTROL ", font="Helvetica 12", bg="#2ECC71", fg="white", width="30", 
                     command= lambda: control())
BTN_control.grid(row=6, column=0, columnspan=10)
#----------------------------------------------------------------
img_register = PhotoImage(file= "./assets/img/registro.png")
sm_register = img_register.subsample(4,4)
registerpng = Label(window, image=sm_register, width="300")
registerpng.grid(row=5, column=10, columnspan=20)

BTN_register = Button(window, text=" TABLERO DE REGISTROS ", font="Helvetica 12", bg="#2ECC71", fg="white", width="30", 
                      command= lambda: registro())
BTN_register.grid(row=6, column=10, columnspan=20)
#----------------------------------------------------------------
img_temp = PhotoImage(file= "./assets/img/temp.png")
sm_temp = img_temp.subsample(2,2)
temppng = Label(window, image=sm_temp, width="300")
temppng.grid(row=7, column=0, columnspan=10)

BTN_reading = Button(window, text=" LECTURA DE SENSORES ", font="Helvetica 12", bg="#2ECC71", fg="white", width="23", 
                     command= lambda: reading())
BTN_reading.grid(row=8, column=0, columnspan=10)
#----------------------------------------------------------------
img_emer = PhotoImage(file= "./assets/img/warning.png")
sm_emer = img_emer.subsample(5,5)
emerpng = Label(window, image=sm_emer, width="300")
emerpng.grid(row=7, column=10, columnspan=20)

BTN_emergency = Button(window, text=" ACTIVAR PARADA DE EMERGENCIA ", font="Helvetica 12", bg="#2ECC71", fg="white", width="35", 
                       command= lambda: emergency())
BTN_emergency.grid(row=8, column=10, columnspan=20)
#----------------------------------------------------------------




window.mainloop()



