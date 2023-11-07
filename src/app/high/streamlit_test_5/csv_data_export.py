import os
import time
from datetime import datetime

from my_date import this_my_local_date as mdate
from my_time import this_my_local_time as mtime

def export_data():
    route = "/src/app/high/streamlit_test_5/loot"
    #route = "./loot/"
    count = 0
    date_f = mdate()
    time_f = mtime()
        
    while True:
        option = input("Cuantas lecturas se necesitan?")
        try:
            option = int(count)
            break
        except ValueError:
            print("El dato ingresado no es valido ingrese un numero")
    
    #file = open(route+"{}_read_sensors.csv".format(date_f), "w")
    file = open(route + "_read_sensors.csv", "w")
    file.write("documento")
    file.close()

    while True:
        #file = open(route+"{}_read_sensors.csv".format(date_f), "a")
        file = open(route + "_read_sensors.csv", "a")
        file.write("\n" + str(date_f) +" "+ str(time_f) + os.linesep)
        file.close()
        count += 1
        # file = open(route+ "{}_read_sensors.csv".format(my_actual_date), "a")
        # # conteo fecha hora senor1 sensor2 sensorn
        # file.write("\n" + str(date_f) +" "+ str(time_f))
        # file.close()
        # count += 1

        if option == count:
            break

export_data()