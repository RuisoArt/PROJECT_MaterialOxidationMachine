import numpy as np
import pandas as pd
import seaborn as sns
import os
from IPython.display import Image

from alerts import no_doc
from alerts import verify_doc
#from . import result

def check_fileindata(window, message):
    #route = "./loot/" # windows
    route = "loot/" #linux

    mensaje = str(message)

    print("El mensaje que llego es: "+str(mensaje))
    dataset = "doc_MaterialOxidationMachine_"+mensaje+".txt"

    try:
        df_sensors = pd.read_csv(route+dataset, sep=" ")
        print(df_sensors.head(3))
        print("Archivo encontrado")
        verify_doc.alert_confirmfile(window, df_sensors, mensaje)
        
    except FileNotFoundError:
        print("Archivo no Encontrado, prueba nuevamente")
        no_doc.alert_no_document()
    #modulo(df_sensors)
