#! /usr/bin/env python3

from tkinter import *
import tkinter as tk
import os

super_route = "/home/onruiso/project/tkinter_test_10/"
# ---------------------------------------------------------------- Funciones extras
route_control = super_route+"Code/control_dash.py"
route_register = super_route+"Context/register_dash.py"
route_read_mcu = super_route+"Database/read_MCU.py"
route_button_emergency = super_route+"Error/button_emergency.py"
back_ground = " &"

def control():
    print("Activado Control")
    os.system("/bin/python3 "+route_control+back_ground)

def registro():
    print("Activado Registro")
    os.system("/bin/python3 "+route_register+back_ground)

#def reading():
#    print("Activado Reading")
os.system("/bin/python3 "+route_read_mcu+back_ground)

#def emergency():
#    print("Activado Button Emergency")
#os.system("/bin/python3 "+route_button_emergency+back_ground) # se traslada a la lectura

# ---------------------------------------------------------------- caracteristicas de la ventana
window = tk.Tk()
window.geometry("1050x750")
window.title("Material Oxidation Machine - Principal Window (by:RuisoArt)")
# ---------------------------------------------------------------- Logos desl sistema
img_rasplogo = PhotoImage(file= super_route+"assets/img/RuisoArt.png")
img_ustalogo = PhotoImage(file= super_route+"assets/img/logo.png")

sm_img_rasp = img_rasplogo.subsample(4,4)
sm_img_usta = img_ustalogo.subsample(5,5)

img_rasp = Label(window, image = sm_img_rasp, width="100")
img_usta = Label(window, image = sm_img_usta, width="200")

img_rasp.grid(row=1, column=0)
img_usta.grid(row=1, column=19)
# ---------------------------------------------------------------- Seccion de header
tittle_primary = Label(window, text = "Software de Control Maquina de Niebla Salina"
                                    +" - Facultad de Ingenieria Mecanica"
                                    +"\nLaboratorio de Materiales"
                                    , font="Helvetica 16", fg="#000000", height=3)
tittle_secundary = Label(window, text = "Proyecto Desarrollado por Ingenieros Electronicos, Mecanicos y de Sistemas de la Universidad Santo Tomas seccional Tunja."
                        , font="Helvetica 10", fg="#000000", height=2, justify="center")

tittle_primary.grid(row=1, column=1, columnspan=18)
tittle_secundary.grid(row=2, column=1, columnspan=18)
# ---------------------------------------------------------------- seccion de img
img_machine = PhotoImage(file= super_route+"assets/img/machine.png")
sm_machine = img_machine.subsample(2,2)
machine = Label(window, image=sm_machine, width="1000")
machine.grid(row=3, column=0, columnspan=20)
#---------------------------------------------------------------- seccion de body
tittle = Label(window, text="Selecciona el Tablero o Software que deseas activar", font="Helvetica 15", fg="#000000", height=2)
tittle.grid(row=4, column=0,  columnspan=20)
#----------------------------------------------------------------
img_control = PhotoImage(file= super_route+"assets/img/control.png")
sm_control = img_control.subsample(4,4)
controlpng = Label(window, image=sm_control, width="300")
controlpng.grid(row=5, column=0, columnspan=10)

BTN_control = Button(window, text=" TABLERO DE CONTROL ", font="Helvetica 12", bg="#2ECC71", fg="white", width="30", 
                     command= lambda: control(), height=2)
BTN_control.grid(row=6, column=0, columnspan=10)
#----------------------------------------------------------------
img_register = PhotoImage(file= super_route+"assets/img/registro.png")
sm_register = img_register.subsample(4,4)
registerpng = Label(window, image=sm_register, width="300")
registerpng.grid(row=5, column=10, columnspan=20)

BTN_register = Button(window, text=" TABLERO DE REGISTROS ", font="Helvetica 12", bg="#2ECC71", fg="white", width="30", 
                      command= lambda: registro(), height=2)
BTN_register.grid(row=6, column=10, columnspan=20)
# #----------------------------------------------------------------
# img_temp = PhotoImage(file= super_route+"assets/img/temp.png")
# sm_temp = img_temp.subsample(2,2)
# temppng = Label(window, image=sm_temp, width="300")
# temppng.grid(row=7, column=0, columnspan=10)

# BTN_reading = Button(window, text=" LECTURA DE SENSORES ", font="Helvetica 12", bg="#2ECC71", fg="white", width="23", 
#                      command= lambda: reading())
# BTN_reading.grid(row=8, column=0, columnspan=10)
# #----------------------------------------------------------------
# img_emer = PhotoImage(file= super_route+"assets/img/warning.png")
# sm_emer = img_emer.subsample(5,5)
# emerpng = Label(window, image=sm_emer, width="300")
# emerpng.grid(row=7, column=10, columnspan=20)

# BTN_emergency = Button(window, text=" ACTIVAR PARADA DE EMERGENCIA ", font="Helvetica 12", bg="#2ECC71", fg="white", width="35", 
#                        command= lambda: emergency())
# BTN_emergency.grid(row=8, column=10, columnspan=20)
# #----------------------------------------------------------------

window.mainloop()



