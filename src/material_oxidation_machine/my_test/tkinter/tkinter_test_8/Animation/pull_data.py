import datetime as dt

import verify_file as very

def pull_dataframe():
    x = dt.datetime.now()
    d = int(x.strftime("%d")) #day
    m = x.strftime("%B")    #month
    y = int(x.strftime("%Y"))   #year
    fecha = str( d )+"_"+ m +"_"+str( y )

    route_doc = "loot/"
    name_doc = str("doc_MaterialOxidationMachine_"+fecha+".txt")

    df_sensors = very.verify_file_loot(fecha)

    return df_sensors

    


