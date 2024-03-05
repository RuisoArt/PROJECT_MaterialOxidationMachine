import random
import time
from generate_text import create_doc

p, ciclos =0, 40 #numero de ciclos para el documento

while True:
    max_count, count, Temp, var1, var2, var3 = 4, 0, random.randint(0, 99), random.randint(0, 99),random.randint(0, 99), random.randint(0, 99)
    create_doc(max_count, count, Temp, var1, var2, var3)
    p = p+1
    if p > ciclos:  break
    else: continue

#print(str( random.randint(0, 99) ) )