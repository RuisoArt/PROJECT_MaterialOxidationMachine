import pandas as pd

def counting(dataframe):
    max = int(dataframe.count())
    lista = []
    for i in range(0, max):
        lista.append(dataframe.loc[:,"nivel"][i])

    conteo = dict(zip(lista,map(lambda x: lista.count(x),lista)))
    print(conteo)
    suma = conteo[0] + conteo[1]
    total_0 = conteo[0]
    total_1 = conteo[1]

    return total_0, total_1, suma
