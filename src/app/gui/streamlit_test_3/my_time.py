import datetime

def this_my_local_time():
    aja = datetime.datetime.now()

    hour = str(aja.hour)
    minute = str(aja.minute)
    seconds = str(aja.second)

    my_date = hour+' : '+minute+' : '+seconds

    return my_date