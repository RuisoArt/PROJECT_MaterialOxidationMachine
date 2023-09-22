def my_decition():
    while True:
        keyboard = input("[1] Encender \n [2] Apagar\n")
        try:
            keyboard = int(keyboard)
            break
        except ValueError:
            print("\n---------------------------------------------------------------")
            print("Ingresa un numero por favor")
            print("---------------------------------------------------------------")

    return keyboard