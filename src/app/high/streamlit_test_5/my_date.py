import datetime

def this_my_local_date():
    aja = datetime.datetime.now()

    day = str(aja.day)
    month = str(aja.month)
    year = str(aja.year)

    time = day+'-'+month+'-'+year

    return str(time)
