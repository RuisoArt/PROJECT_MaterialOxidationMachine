def my_keyboard():
    while True:
        keyboard = input("Ingresa la salida a utilizar: \n")
        try:
            keyboard = int(keyboard)
            break
        except ValueError:
            print("\n---------------------------------------------------------------")
            print("Ingresa un numero por favor")
            print("---------------------------------------------------------------")

    return keyboard