import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
out_0 = 32 #GPIO 12   compresor, resistencia
out_1 = 36 #GPIO 16   hornillo, toma disponible
out_2 = 38 #GPIO 20   luminarias delanteras
out_3 = 40 #GPIO 21   luminarias traseras

pin0 = out_0
pin1 = out_1
pin2 = out_2
pin3 = out_3

GPIO.setup(pin0, GPIO.OUT)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

def init_gpio():
    GPIO.output(pin0,0)
    GPIO.output(pin1,0)
    GPIO.output(pin2,0)
    GPIO.output(pin3,0)

def menu_aviso():
    print("-------------------------------------------------")
    print("                    AVISO: ")
    print("-------------------------------------------------")
    print("Antes de continuar tenga en cuenta lo siguiente: \n\n")
    print("Actualmente solo existen 4 pines configurados en la \n"
          "RaspBerry que sirven como salidas, las mismas están \n"
          "conectadas de las siguientes maneras:\n\n")
    print("1. Salida 1, conectada para encender el Compresor \n"
          "de Aire y la Resistencia de Calentamiento del agua.\n\n")
    print("2. Salida 2, conectada para encender el hornillo o \n"
            "la toma disponible en 120vAC.\n\n")
    print("3. Salida 3, conectada para encender las luminarias \n traseras.\n\n")
    print("4. Salida 4, conectada para encender las luminarias \n delanteras.\n\n")
    print("Importante: Recuerda revisar que tu teclado numerico este habilitado.")
    print("-------------------------------------------------\n\n\n")

def menu_options():
    print("---------------------------------------------------------------")
    print("             Menu conmutacion de salidas")
    print("---------------------------------------------------------------")
    print("Selecciona la salida o salidas a activar o desactivar: \n")

    print("[1] Luminarias Delanteras.")
    print("[2] Luminarias Traseras.")
    print("[3] Todas las luminarias.")

    print("[4] Hornillo y Toma Disponible AC.")
    print("[5] Compresor y Resistencia.")
    print("[6] Compresor, Resistencia, Hornillo y Toma Disponible.")

    print("[7] Todo el sistema de Conmutacion.")
    print("[0] Salir del Programa de conmutacion")
    print("---------------------------------------------------------------")

def menu_initialized():
    menu_aviso()

    while True:  
        menu_options()
        
        while True:
            print("---------------------------------------------------------------")
            keyboard = input("Ingresa la salida a utilizar: \n")
            try:
                keyboard = int(keyboard)
                break
            except ValueError:
                print("\n---------------------------------------------------------------")
                print("Ingresa un numero por favor")
                print("---------------------------------------------------------------")

        if keyboard == 0:
            print("\n\n\n---------------------------------------------------------------")
            print("---------------------------------------------------------------")
            print("Saldra del menu de conmutacion.")
            print("---------------------------------------------------------------")
            break

        elif keyboard == 1:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 1 del menu en ejecucion.")
                GPIO.output(pin0, 1)
                print("La Salida 1 se ha encendido")
            elif key == 2:
                print("Apagando, opcion 1 del menu en ejecucion.")
                GPIO.output(pin0, 0)
                print("La Salida 1 se ha apagado")
            else:
                print("Opcion no valida")

        elif keyboard == 2:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 2 del menu en ejecucion.")
                GPIO.output(pin1, 1)
                print("La Salida 2 se ha encendido")
            elif key ==2:
                print("Apagando, opcion 2 del menu en ejecucion.")
                GPIO.output(pin1, 0)
                print("La Salida 2 se ha apagando")
            else:
                print("No es una opcion")
            
        elif keyboard == 3:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 3 del menu en ejecucion.")
                GPIO.output(pin0, 1)
                GPIO.output(pin1, 1)
                print("La Salida 1 y Salida 2 se han encendido")
            elif key == 2:
                print("Apagando, opcion 3 del menu en ejecucion.")
                GPIO.output(pin0, 0)
                GPIO.output(pin1, 0)
                print("La Salida 1 y Salida 2 se han apagado")
            else:
                print("Opcion no valida")

        elif keyboard == 4:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 4 del menu en ejecucion.")
                GPIO.output(pin2, 1)
                print("La Salida 4 se ha encendido")
            elif key ==2:
                print("Apagando, opcion 4 del menu en ejecucion.")
                GPIO.output(pin2, 0)
                print("La Salida 4 se ha apagando")
            else:
                print("Entrada por teclado no valida")

        elif keyboard == 5:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 5 del menu en ejecucion.")
                GPIO.output(pin3, 1)
                print("La Salida 3 se ha encendido")
            elif key==2:
                print("Apagando, opcion 5 del menu en ejecucion.")
                GPIO.output(pin3, 0)
                print("La Salida 3 se ha Apagado")
            else:
                print("No valido")

        elif keyboard == 6:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n [2] Apagar\n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 6 del menu en ejecucion.")
                GPIO.output(pin2, 1)
                GPIO.output(pin3, 1)
                print("La Salida 3 y Salida 4 se han encendido")
            elif key==2:
                print("Apagando, opcion 6 del menu en ejecucion.")
                GPIO.output(pin2, 0)
                GPIO.output(pin3, 0)
                print("La Salida 3 y Salida 4 se han apagado")
            else:
                print("No valido")
        
        elif keyboard == 7:
            while True:
                print("\n---------------------------------------------------------------")
                key = input("[1] Encender \n[2] Apagar \n")
                try:
                    key=int(key)
                    break
                except ValueError:
                    print("No es una opcion")
            if key == 1:
                print("Encendiendo, opcion 7 del menu en ejecucion.")
                GPIO.output(pin0, 1)
                GPIO.output(pin1, 1)
                GPIO.output(pin2, 1)
                GPIO.output(pin3, 1)
                print("La Salida 1, Salida 2, Salida 3 y Salida 4 se han encendido")
            elif key==2:
                print("Apagando, opcion 7 del menu en ejecucion.")
                GPIO.output(pin0, 0)
                GPIO.output(pin1, 0)
                GPIO.output(pin2, 0)
                GPIO.output(pin3, 0)
                print("La Salida 1, Salida 2, Salida 3 y Salida 4 se han apagado")
            else:
                print("No valido")

        else:
            print("No se ha seleccionado una salida valida")

# La ejecucion
init_gpio()
menu_initialized()