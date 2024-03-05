import tkinter

#la ventana:
window = tkinter.Tk()
window.geometry("700x400") # tamaño de la ventana anchoxAlto

# -..................................POSICIONAR LOS WIDGETS CON EL METODO GRID ..............................

btn1 = tkinter.Button(window, text="Button 1", padx=30, pady=10)
btn2 = tkinter.Button(window, text="Button 2", padx=30, pady=10)
btn3 = tkinter.Button(window, text="Button 3", padx=30, pady=10)
#btn4 = tkinter.Button(window, text="Button 4", width=30 , height=10)
btn4 = tkinter.Button(window, text="Button 4", padx=30 , pady=10)
btn5 = tkinter.Button(window, text="Button 5", padx=30 , pady=10)
btn6 = tkinter.Button(window, text="Button 6", padx=30, pady=10)

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)
btn2.grid(row=2, column=2)
btn3.grid(row=3, column=3)
btn4.grid(row=4, column=4)
btn5.grid(row=5, column=5)
btn6.grid(row=6, column=6)
    


window.mainloop()