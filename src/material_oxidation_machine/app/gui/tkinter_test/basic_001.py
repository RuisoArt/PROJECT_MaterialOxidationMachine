from tkinter import * # importar todo

import tkinter

#la ventana:
window = tkinter.Tk()

window.geometry("700x400") # tamaño de la ventana anchoxAlto

label = tkinter.Label(window, text="Hola Mundo", bg="#00FF00")
label.pack() # centrado de la ventana ARRIBA

window.mainloop()