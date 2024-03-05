import tkinter

#la ventana:
window = tkinter.Tk()
window.geometry("700x400") # tamaño de la ventana anchoxAlto

# ----------------------------------------- Botones -----------------------------------------------------------
def hi():
    print("Hello my fucking world!")

button1 = tkinter.Button(window, text="Presiona Aqui", padx=40 , pady=40, command=hi)
# hi => se activa con la presion del boton la funcion (esta es la que se utiliza)
# hi() => la funcion se activa apenas se inicia el programa, pero queda aislada del boton, como si se hubiera invocado por aparte
button1.pack()

window.mainloop()