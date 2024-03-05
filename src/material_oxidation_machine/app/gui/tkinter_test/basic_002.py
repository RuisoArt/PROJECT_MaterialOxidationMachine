import tkinter

#la ventana:
window = tkinter.Tk()
window.geometry("700x400") # tamaño de la ventana anchoxAlto

label = tkinter.Label(window, text="Hola Mundo", bg="#00FF00")

#.......................................... Metodo PACK ...................................................
# side => posicionar
# fill => estirar

label.pack() # centrado de la ventana ARRIBA
label.pack(side = tkinter.BOTTOM) # centrado de la ventana ABAJO
label.pack(side = tkinter.RIGHT) # centrado de la ventana DERECHA
label.pack(side = tkinter.LEFT) # centrado de la ventana IZQUIERDA

label.pack(fill= tkinter.X) # Expande el cuadro del texto en horizontal
label.pack(fill= tkinter.Y, expand = True) # Expande el cuadro del texto en vertical
label.pack(fill= tkinter.BOTH, expand=True) # Expande el cuadro de texto a toda la ventana

window.mainloop()