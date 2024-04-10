from tkinter import *
import tkinter as tk

from header import my_second_header
#from .code.history.cipher_body.body import my_second_body
#from .code.history.cipher_body.second_body import my_second_body
from body import the_body

super_route = "/home/onruiso/project/tkinter_test_10/"
icono = super_route+"assets/img/USTAcarpeta.ico"
#----------------------------------------------------------------
window = tk.Tk()
window.geometry("1030x850")
window.title("Material Oxidation Machine Data Register History (by: RuisoArt)")
#window.iconbitmap(icono)
# ----------------------------------LOGOS------------------------------
img_rasplogo = PhotoImage(file= super_route+"assets/img/RuisoArt.png")
img_ustalogo = PhotoImage(file= super_route+"assets/img/logo.png")

sm_img_rasp = img_rasplogo.subsample(5,5)
sm_img_usta = img_ustalogo.subsample(5,5)

img_rasp = Label(window, image = sm_img_rasp, width="100")
img_usta = Label(window, image = sm_img_usta, width="200")

img_rasp.grid(row=1, column=0)
img_usta.grid(row=1, column=19)
#---------------------------------------------------------------
my_second_header(window)
#----------------------------------------------------------------
the_body(window)



window.mainloop()