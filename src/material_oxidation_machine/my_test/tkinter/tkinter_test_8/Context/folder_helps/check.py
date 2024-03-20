import math
from alerts import verify
from alerts import not_num
from alerts import out_range
from settings import graph

def check_integer(var):
    try:
        var = int(var)
        #verify.alert_verify()
        if var > 0:
            return var
        else:
            return False
    except ValueError as e:
        not_num.alert_not_number()
        return False 
    
def check_rangeofmonth(var):
    month = int(var)
    if month > 0 and month <= 12:
        if month == 1:
            month="January"
        elif month == 2:
            month="February"
        elif month == 3:
            month="March"
        elif month == 4:
            month="April"
        elif month == 5:
            month="May"
        elif month == 6:
            month="June"
        elif month == 7:
            month="July"
        elif month == 8:
            month="August"
        elif month == 9:
            month="September"
        elif month == 10:
            month="October"
        elif month == 11:
            month="November"
        elif month == 12:
            month="December"
        return month
    else:
        out_range.alert_out_of_range_month()
        return False
        
def check_rangeofday(var):
    day = int(var)
    if day > 0 and day <= 31:
        day = str(day)
        return day
    else:
        out_range.alert_out_of_range_day()
        return False  

def check_hourrange(window, hourmin, in_hour_min, hourmax, in_hour_max, df_sensors):
    #comprobacion de enteros o si es false
    inhourmin = in_hour_min.get()
    inhourmax = in_hour_max.get()
    inhourmin = int(inhourmin) #* 10000
    inhourmax = int(inhourmax) #* 10000

    hourmin = hourmin.replace('hora', '')
    hourmin = hourmin.replace('dtype: int64', '')
    hourmin = hourmin.replace('\n', '')
    hourmin = int(hourmin)
    deci1, hourmin = math.modf( hourmin/10000 )
    hourmin = int(hourmin)
    
    hourmax = hourmax.replace('hora', '')
    hourmax = hourmax.replace('dtype: int64', '')
    hourmax = hourmax.replace('\n', '')
    hourmax = int(hourmax)
    deci2, hourmax = math.modf( hourmax/10000 )
    hourmax = int(hourmax)

    print("Hora de archivo es: "+str(hourmin)+" Hora de entrada: "+str(inhourmin))
    print("Hora de archivo es: "+str(hourmax)+" Hora de entrada: "+str(inhourmax))
        
    inhourmin = check_integer(inhourmin)
    print("paso inhourmin: "+str(inhourmin))
    inhourmax = check_integer(inhourmax)
    print("paso inhourmax: "+str(inhourmax))
    hourmin = check_integer(hourmin)
    print("paso hourmin: "+str(hourmin))
    hourmax = check_integer(hourmax)
    print("paso hourmax: "+str(hourmax))
    
    my_minh, my_maxh = 0,0

    if hourmin == False or inhourmin == False or hourmax == False:
        print("No son numeros")
    elif inhourmin >= hourmin and inhourmin <= hourmax:
        my_minh = inhourmin
    else:
        out_range.alert_out_of_hour()

    # print("Hora de archivo es: "+str(hourmin)+" Hora de entrada: "+str(inhourmin))
    # print("Hora de archivo es: "+str(hourmax)+" Hora de entrada: "+str(inhourmax))

    if hourmin == False or hourmax == False or inhourmax == False:
        print("No son numeros")
    elif inhourmax >= hourmin and inhourmax <= hourmax:
        my_maxh = inhourmax
    else:
        out_range.alert_out_of_hour()

    print("hora minima que llega: "+str(my_minh)+" hora maxima que llega: "+str(my_maxh))

    if my_maxh != 0 and my_minh != 0:
        graph.my_grah(window, my_minh, my_maxh, df_sensors)
    else:
        print("las horas son ceros")
        out_range.alert_out_of_hour()
        

