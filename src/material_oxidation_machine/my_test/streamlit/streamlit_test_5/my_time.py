#pip install DateTime
from datetime import datetime
import time

def this_my_local_time():
    dt = datetime.now()
    my_time = datetime.strftime(dt, "%H:%M:%S")

    return str(my_time)
