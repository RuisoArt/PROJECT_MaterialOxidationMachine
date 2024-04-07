from tkinter import *
import tkinter as tk

from header import my_header
from body import my_body

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
