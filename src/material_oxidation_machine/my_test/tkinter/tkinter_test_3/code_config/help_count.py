import tkinter as tk
from tkinter import ttk


def sumar():
    produccion.set(str(int(produccion.get()) + 1))     


raiz = tk.Tk()
produccion = tk.StringVar(raiz, "0")
prod = tk.Entry(raiz, textvariable=produccion)
prod.pack(side=tk.TOP)
contador = ttk.Button(raiz, text="sumador", command=sumar)
contador.pack(side=tk.BOTTOM)

raiz.mainloop() 