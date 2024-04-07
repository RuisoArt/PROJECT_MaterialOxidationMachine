import pandas as pd

def counting(dataframe):
    max = int(dataframe.count())
    lista = []
    for i in range(0, max):
        lista.append(dataframe.loc[:,"nivel"][i])

    conteo = dict(zip(lista,map(lambda x: lista.count(x),lista)))
    print(conteo)
    print("tamaño de conteo:"+str(len(conteo)))

    try:
        numero0 = conteo[0]
        print("exite valor de 0: "+str(numero0))
    except:
        print("No existe valor de 0")
        numero0 = 0
    
    try:
        numero1 = conteo[1]
        print("exite valor de 1: "+str(numero1))
    except:
        print("No existe valor de 1")
        numero1 = 0
   

    suma = numero0 + numero1
    total_0 = numero0
    total_1 = numero1

    return total_0, total_1, suma
