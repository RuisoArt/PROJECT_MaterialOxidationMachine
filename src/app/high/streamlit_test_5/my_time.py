#pip install DateTime
from datetime import datetime
import time

def this_my_local_time():
    dt = datetime.now()
    my_time = datetime.strftime(dt, "%H:%M:%S")
    print(my_time)

    return str(my_time)

this_my_local_time()