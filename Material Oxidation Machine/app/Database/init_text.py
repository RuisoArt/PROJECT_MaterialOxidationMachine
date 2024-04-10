import random
import time
import datetime as dt
from generate_text import create_doc

def init_register(Temp, var1, var2, var3):

    #p, ciclos =0, 200 #numero de ciclos para el documento

    #while True:
    x = dt.datetime.now()
    fecha = str( x.strftime("%d") +"_"+ x.strftime("%B") +"_"+ x.strftime("%Y") )
    hora = str( x.strftime("%H")) + str(x.strftime("%M")) + str(x.strftime("%S")) 
    max_count, count = 0, 0
    create_doc(max_count, count, fecha, hora, Temp, var1, var2, var3)
        # p = p+1
        # if p > ciclos:  break
        # else: continue

#print(str( random.randint(0, 99) ) )