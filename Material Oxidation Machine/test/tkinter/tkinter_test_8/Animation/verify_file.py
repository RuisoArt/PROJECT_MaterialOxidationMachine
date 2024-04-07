import numpy as np
import pandas as pd

def verify_file_loot(name_doc):
    route = "loot/" #linux

    print("El mensaje que llego es: "+str(name_doc))
    dataset = "doc_MaterialOxidationMachine_"+str(name_doc)+".txt"

    try:
        df_sensors = pd.read_csv(route+dataset, sep=" ")
        print(df_sensors.head(3))
        print("Archivo encontrado")
        #verify_doc.alert_confirmfile(window, df_sensors, mensaje)
        return df_sensors
        
    except FileNotFoundError:
        print("Archivo no Encontrado, prueba nuevamente")
        dt_vacio = pd.DataFrame()
        return dt_vacio
        #no_doc.alert_no_document()
    #modulo(df_sensors)