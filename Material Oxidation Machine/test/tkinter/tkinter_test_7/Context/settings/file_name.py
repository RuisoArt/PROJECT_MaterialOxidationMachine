import numpy as np
import pandas as pd
import seaborn as sns
import os
from IPython.display import Image

from folder_helps import check
from alerts import not_num
from alerts import verify
from . import confirm_file
from . import result

def my_file_name(window, year, month, day):

    var_year = year.get()
    var_month = month.get()
    var_day = day.get()
    
    my_year = check.check_integer(var_year)
    my_month = check.check_integer(var_month)
    my_month = check.check_rangeofmonth(my_month)
    my_day = check.check_integer(var_day)
    my_day = check.check_rangeofday(my_day)

    if my_year == False or my_month == False or my_day == False:
        not_num.alert_not_number()
    else:
        carta = str(my_day)+"_"+str(my_month)+"_"+str(my_year)
        print("El mensaje que sale es: "+str(carta))
        #verify.alert_verify()
        confirm_file.check_fileindata(window, carta)

   
    