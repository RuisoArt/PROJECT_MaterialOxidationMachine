from tkinter import *
import tkinter as tk
from header import my_header
from body import my_body
import os

# pendiente de reemplazo de ruta para despues el ejecutable y minimizar a ruta general de archivo
#os.system("/bin/python3 /home/onruiso/Desktop/Software/tkinter_test_8/Database/read_MCU.py &")
#os.system("/bin/python3 /home/onruiso/Desktop/Software/tkinter_test_8/Error/button_emergency.py &")

route_read_mcu = "/home/onruiso/project/tkinter_test_9/Database/read_MCU.py"
route_button_emergency = "/home/onruiso/project/tkinter_test_9/Error/button_emergency.py"
back_ground = " &"  

os.system("/bin/python3 "+route_read_mcu+back_ground)
os.system("/bin/python3 "+route_button_emergency+back_ground)

#------------------------------ Caracteristicas de la ventana ----------------------------------
window = tk.Tk()
window.geometry("1170x550")
window.title("Material Oxidation Machine - Local Control Software (by:RuisoArt)")
#window.iconbitmap(".assets/img/USTAcarpeta.ico")
# ----------------------------------LOGOS------------------------------
img_rasplogo = PhotoImage(file= "./assets/img/COLOURRaspberryPI.png")
img_ustalogo = PhotoImage(file= "./assets/img/logo.png")

sm_img_rasp = img_rasplogo.subsample(5,5)
sm_img_usta = img_ustalogo.subsample(5,5)

img_rasp = Label(window, image = sm_img_rasp, width="100")
img_usta = Label(window, image = sm_img_usta, width="200")

img_rasp.grid(row=1, column=0)
img_usta.grid(row=1, column=19)

# ------------------------------- Seccion HEADER de la ventana ---------------------------------
my_header(window)
# -------------------------------- Seccion BODY de la Ventana ----------------------------------
my_body(window)
# -----------------------------------------------------------------------------------------------

window.mainloop()
