import datetime as dt
import os
import time

x = dt.datetime.now()
fecha = str( x.strftime("%d") +"_"+ x.strftime("%B") +"_"+ x.strftime("%Y") )
hora = str( x.strftime("%X") )
route_doc = "loot/"
name_doc = str("doc_MaterialOxidationMachine_"+fecha+".txt")

def init_document(route_doc, name_doc):
    # with open(str(route_doc+name_doc),"w") as file:
    #     file.write("count Temp var1 var2 var3")

    file = open(str(route_doc+name_doc),"x")
    file.close()

    file = open(str(route_doc+name_doc),"a")
    file.write("fecha hora temp1 temp2 temp3 nivel")
    file.close()

def write_doc(message):
    file = open(str(route_doc+name_doc), "a")
    file.write("\n"+str(message))
    file.close()

def create_doc(max_count, count, fecha, hora, Temp, var1, var2, var3):
    # probar si el documento existe o no en la ruta 
    print("Buscando archivo en la ruta: ("+route_doc+")")
    try:
        myfile = open(str(route_doc+name_doc))
        print("Si existe el archivo")
        myfile.close()
    except FileNotFoundError: 
        print("Archivo no encontrado en la ruta ("+route_doc+"), Creando archivo")
        init_document(route_doc, name_doc)
      

    while True:
        message = fecha+" "+hora+" "+str(Temp)+" "+str(var1)+" "+str(var2)+" "+str(var3)
        print( message )
        write_doc(message)
        print( "write doc" )
        count = count + 1
        time.sleep(0.125) # 1/8 de segundo

        if count > max_count:
            break
        else:
            continue


#create_doc(3, 0, 0, 0, 0, 0)