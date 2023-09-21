"""
lectura simple: https://putosistema.wordpress.com/2017/08/27/leer-puerto-serial/
comuniacion serial: https://programmerclick.com/article/42921672706/

pip install pyserial => windows so
"""

import serial
from time import sleep
import datetime
import time
import os

def proube_numeric(text):
    while True:
        key = input(text)
        try:
            key = int(key)
            break
        except ValueError:
            print("Dato ingresado no valido")
    return key

def process_time():
    print("-------------------------------------------------------------------")
    print("         Definir tiempo de captura de datos")
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

def local_time():
    current_time = datetime.datetime.now().time()
    current_hour    = current_time.hour         #regresa la hora actual
    current_minute  = current_time.minute       #regresa el minuto actual
    current_second  = current_time.second       #regresa el segundo actual
    init_time = str(current_hour)+":"+str(current_minute)+":"+str(current_second)
    return init_time

def local_date():
    current_date = datetime.datetime.now().date()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year
    init_date = str(current_day)+":"+str(current_month)+":"+str(current_year)
    return init_date

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


# en windows se pregunta por com en linux por la ruta especifica del sistema

# windows:
ser = serial.Serial("COM5",115200)
ls = str(os.getcwd()).replace('\\','/')
route = ls+'/code/ZonaTest/test_3/samples_doc/'

my_date = local_date()
my_time = local_time()
menssage = str(my_date+","+my_time)

#estado = True

#final_time, final_hour, final_minute, final_second = process_time()
#i_hour, i_minute, i_second = 0,0,0
#estado = process_timer_now(True, final_hour, final_minute, final_second, i_hour, i_minute, i_second)

try:
    #ser = serial.Serial("COM6",115200)
    ser.setDTR(False)
    sleep(1)
    ser.flushInput()
    ser.setDTR(True)

    while True:
        data = ser.readline()
        my_string = str(data)

        print("\n----------------------------------------------------")
        print("               Lectura de sensores")
        print("----------------------------------------------------")
        print("Acontinuacion ingrese los datos que son solicitados")
        print("\n")

        my_string = my_string.replace('b','')
        my_string = my_string.replace('r','')
        my_string = my_string.replace('n','')
        my_string = my_string.replace('str(\\)','')
        #my_string = data.decode('ascii')
        print(my_string)

        file = open(route+'{}.csv'.format(my_date),"a")
        file.write('\n'+menssage)
        file.close()

except:
    print("Error")


ser.close()


    