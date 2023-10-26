import os
import time

from my_date import this_my_local_date
from my_time import this_my_local_time

def export_data():
    count = 0
    route = './src/app/high/streamlit_test_5/botin/'

    date = 1#this_my_local_date
    time = 1#this_my_local_time
    count_max = int(input("Cuanto quieres que dure el conteo? "))

    message = 'La fecha es: '+str(date)+' La hora es: '+str(time)+' Este es el registro numero: '+str(count_max)

    while True:
        if count != count_max:
            file = open(route+'{}.csv'.format(date),"a")
            file.write('\n'+message)
            file.close()
            
            count += 1
        else:
            break

export_data()    