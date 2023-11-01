#pip install DateTime
from datetime import datetime
import time

def this_my_local_date():
    dt = datetime.now()
    my_day      = datetime.strftime(dt, '%d')
    my_month    = datetime.strftime(dt, '%m')
    my_year     = datetime.strftime(dt, '%Y')

    my_date = str(my_day) +"/"+ str(my_month) +"/"+ str(my_year)
    print(my_date)

    return my_date

