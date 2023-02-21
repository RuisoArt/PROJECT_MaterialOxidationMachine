#Notas: Tener en cuenta que el maximo de horas puestas puede sobrepasar dias, meses en el calendario
# boton de cancelacion pendiente

import datetime
import time
import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
out_0 = 32 #GPIO 12   compresor, resistencia
out_1 = 36 #GPIO 16   hornillo, toma disponible
out_2 = 38 #GPIO 20   luminarias delanteras
out_3 = 40 #GPIO 21   luminarias traseras
GPIO.setup(out_0, GPIO.OUT)
GPIO.setup(out_1, GPIO.OUT)
GPIO.setup(out_2, GPIO.OUT)
GPIO.setup(out_3, GPIO.OUT)

def init_gpio():
    GPIO.output(out_0,0)
    GPIO.output(out_1,0)
    GPIO.output(out_2,0)
    GPIO.output(out_3,0)

def proube_numeric(text):
    while True:
        key = input(text)
        try:
            key = int(key)
            break
        except ValueError:
            print("Dato ingresado no valido")
    return key

def local_time():
    current_time = datetime.datetime.now().time()
    current_hour    = current_time.hour         #regresa la hora actual
    current_minute  = current_time.minute       #regresa el minuto actual
    current_second  = current_time.second       #regresa el segundo actual
    init_time = str(current_hour)+":"+str(current_minute)+":"+str(current_second)
    return init_time

def process_time():
    print("-------------------------------------------------------------------")
    print("         Definir tiempos de trabajo de la Maquina")
    print("-------------------------------------------------------------------")
    while True:
        final_hour = proube_numeric("Ingresa el numero de horas a trabajar: ")
        if 0 <= final_hour: break 
        else: print("Numero fuera de rango")
    while True:
        final_minute = proube_numeric("Ingresa el numero de minutos a trabajar: ")
        if 0 <= final_minute < 60: break
        else: print("Numero fuera de limites.")
    while True:
        final_second = proube_numeric("Ingresa el numero de segundos a trabajar: ")
        if 0 <= final_second < 60: break
        else: print("Numero fuera de rango")
    print("-------------------------------------------------------------------")
    final_time = str(final_hour)+":"+str(final_minute)+":"+str(final_second)
    return final_time, final_hour, final_minute, final_second

def process_timer_now(ready, f_hour, f_minute, f_second, i_hour, i_minute, i_second):
    while True:
        i_second += 1
        time.sleep(1)
        if i_second == 59:
            i_second = 0
            i_minute += 1

            if i_minute == 59:
                i_minute = 0
                i_hour += 1

        elif i_hour == f_hour and i_minute == f_minute and i_second == f_second:
            print("Proceso finalizado")
            i_hour, i_minute, i_second = 0,0,0
            final_hour, final_minute, final_second = 0,0,0
            break
        
        in_process = str(i_hour)+":"+str(i_minute)+":"+str(i_second)
        print("Time: "+in_process)
    
    return False

init_gpio()
initializer = local_time()
finalization, f_hour, f_minute, f_second = process_time()
i_hour, i_minute, i_second = 0,0,0
ready = True
print("El tiempo real de inicio es: "+initializer)
print("El tiempo que durara la maquina encendida es: "+finalization)
print("El tiempo inicia ahora en 00:00:00, podra ver el progreso en pantalla")

print("----------------------------")
print("Sistema iniciado")
print("----------------------------")
GPIO.output(out_0,1)
GPIO.output(out_1,1)
GPIO.output(out_2,1)
GPIO.output(out_3,1)

ready = process_timer_now(ready, f_hour, f_minute, f_second, i_hour, i_minute, i_second)

if ready == True:
    GPIO.output(out_0,1)
    GPIO.output(out_1,1)
    GPIO.output(out_2,1)
    GPIO.output(out_3,1)

elif ready == False:
    print("----------------------------")
    print("Sistema Apagado")
    print("----------------------------")
    GPIO.output(out_0,0)
    GPIO.output(out_1,0)
    GPIO.output(out_2,0)
    GPIO.output(out_3,0)
    


