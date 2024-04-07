import pandas as pd

from foder_body import zone_datainfo as dinfo
from folder_helps import count_data as ccdd

def show_generaldata_ofDataframe(window, dataset, mensaje):
    print("dataframe recibido mother fucker")
    df_sensors = dataset
    print(df_sensors.head(3))

    #----------------------------------------------------------------Titulo del documento
    df_hour = pd.DataFrame(df_sensors.loc[:, 'hora'])
    titulo = str( "doc_MaterialOxidationMachine_" + str(mensaje) + ".txt")
    quantity = str( df_hour.count() )
    hourmin = str(df_hour.min())
    hourmax = str(df_hour.max())
    print("\n")
    #----------------------------------------------------------------temperature 1
    df_temp1        = pd.DataFrame(df_sensors.loc[:, 'temp1'])
    temp1min        = str( df_temp1.min() )
    temp1max        = str( df_temp1.max() )
    temp1media      = str( df_temp1.mean() )
    temp1mediana    = str( df_temp1.median() )
    print("\n")
    #----------------------------------------------------------------temperatura 2
    df_temp2        = pd.DataFrame(df_sensors.loc[:, 'temp2'])
    temp2min        = str( df_temp2.min() )
    temp2max        = str( df_temp2.max() )
    temp2media      = str( df_temp2.mean() )
    temp2mediana    = str( df_temp2.median() )
    print("\n")
    #----------------------------------------------------------------temperatura 3
    df_temp3 = pd.DataFrame(df_sensors.loc[:, 'temp3'])
    temp3min = str( df_temp3.min() )
    temp3max = str( df_temp3.max() )
    temp3media = str( df_temp3.mean() )
    temp3mediana = str( df_temp3.median() )
    print("\n")
    #----------------------------------------------------------------nivel
    #print("Calumna a graficar: "+str(df_sensors.keys()[5]))
    df_nivel = pd.DataFrame(df_sensors.loc[:, 'nivel'])
    lv_total_0, lv_total_1, lv_suma  = ccdd.counting(df_nivel)

    # print("Nivel Minimo Registrada : "+ str( df_nivel.min() ) )
    # print("Nivel Maximo Registrada : "+ str( df_nivel.max() ) )
    # print("Nivel Medio Registrada : "+ str( df_nivel.mean() ) )
    # print("Nivel Mediano Registrada : "+ str( df_nivel.median() ) )
    print("\n")
    #----------------------------------------------------------------
    dinfo.dataset_info(window, titulo, quantity, hourmin, hourmax,
                       temp1min, temp1max, temp1media, temp1mediana,
                       temp2min, temp2max, temp2media, temp2mediana,
                       temp3min, temp3max, temp3media, temp3mediana,
                       lv_total_0, lv_total_1, lv_suma)




    # el nivel hay aque anotar el porcentaje de unos contra porcentajes de ceros y no tiene mucho sentido el minimo y maximo registrado pues es unos y ceros
