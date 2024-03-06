from alerts import verify
from alerts import not_num
from alerts import out_range

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

def check_hourmin(window, var):

def check_hourmax(window, var):