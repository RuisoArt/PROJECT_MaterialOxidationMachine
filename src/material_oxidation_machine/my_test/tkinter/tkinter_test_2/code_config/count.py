from tkinter import *
import tkinter as tk
import time

def visible_count(window):
    option = 2
    while True:
        if option <= 0:
            conteo = Label(window,text=str(option)+" Finished!"
                       ,bg="#212F3D", font="Helvetica 12", fg="#FFFFFF")
            conteo.grid(row=5, column=7)
            break

        elif option > 0:
            conteo = Label(window,text=str(option)
                        ,bg="#212F3D", font="Helvetica 12", fg="#FFFFFF")
            conteo.grid(row=5, column=7)
            time.sleep(1)
            option = option - 1
        
        else:
            conteo = Label(window,text="error"
                        ,bg="#212F3D", font="Helvetica 12", fg="#FFFFFF")
            conteo.grid(row=5, column=7)
