import tkinter

#la ventana:
window = tkinter.Tk()
window.geometry("700x400") # tamaño de la ventana anchoxAlto

# .....................................Entradas de texto ................................

TextBox = tkinter.Entry(window, font="Helvetica 20")
TextBox.pack()

labelText = tkinter.Label(window)
labelText.pack()

def textTerminal():
    myText = TextBox.get()
    print("se recibio lo siguiente = "+ myText) # escribir texto en la terminal
    labelText["text"] = myText # Escribir texti en una etuqieta

button = tkinter.Button(window, text="Send", command=textTerminal)
button.pack()

window.mainloop()