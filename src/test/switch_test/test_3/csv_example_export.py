# date, hours, number, sample, \n

import os
from datetime import datetime
import time

ls = str(os.getcwd()).replace('\\','/')
#route = ls+'/code/ZonaTest/test_3/samples_doc/'
route = ls

minute = 60
hour   = 3600

now = datetime.now()
my_date = str(now.day)+'-'+str(now.month)+'-'+str(now.year)
my_time = str(now.hour)+':'+str(now.minute)+':'+str(now.second)

menssage = str(my_date+","+my_time)

def menu_program():
    count = 0

    print("\n----------------------------------------------------")
    print("               Lectura de sensores")
    print("----------------------------------------------------")
    print("Acontinuacion ingrese los datos que son solicitados")
    print("\n")

    while True:
        time_exec = input("¿Cuanto tiempo van a tomarse las lecturas? (horas): ")
        try:
            time_exec = int(time_exec)
            break
        except ValueError:
            print("El dato ingresado no es valido, intentelo de nuevo")

    while True:
        time_sample = input("¿Cada cuanto necesita que se tomen lecturas?(minutos): ")
        try:
            time_sample = int(time_sample)
            break
        except ValueError:
            print("El dato ingresado no es valido, intentelo de nuevo")

    time_exec = time_exec * minute
    time_sample = time_sample * minute

    print("\n El proceso durara {} horas y se tomara "
            +"una muestra de los sensores cada {} minutos".format(time_exec, time_sample))

    while True:
        file = open(route+'{}.csv'.format(my_date),"a")
        file.write('\n'+menssage)
        file.close()
        time.sleep(time_sample)



#print("fecha: ",my_date," hora: ",my_time)