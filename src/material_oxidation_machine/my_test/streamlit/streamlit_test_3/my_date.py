import datetime

def this_my_local_date():
    aja = datetime.datetime.now()

    day = aja.day
    month = aja.month
    year = aja.year

    time = str(day) +'-'+ str(month) +'-'+ str(year)

    return print(str(time))
