from tkinter import *
import tkinter as tk

from header import my_header
from body import my_body

#------------------------------ Caracteristicas de la ventana ----------------------------------
window = tk.Tk()
window.geometry("1300x700")
window.title("Material Oxidation Machine - Local Control Software (by:RuisoArt)")
#-----------------------------------------------------------------------------------------------

# ------------------------------- Seccion HEADER de la ventana ---------------------------------
my_header(window)
# -------------------------------- Seccion BODY de la Ventana ----------------------------------
my_body(window)



window.mainloop()
