import streamlit as st
from annotated_text import annotated_text
from web_params import input_params

def my_column():    
    #var1, var2, var3, var4, var5, var6, var7 = 0,0,0,0,0,0,0 # hay que ver que no se reseteen cada que se ejecute OJO!
    #var1, var2, var3, var4, var5, var6, var7 = "Apagado","Apagado","Apagado","Apagado","Apagado","Apagado","Apagado"
    #variables de conmutacion, estados
    st.sidebar.header("Menu de Conmutacion \n Salidas de Control ON / OFF \n Maquina de Niebla Salina.\n\n")

    # options = [
    #     "[1] Luminarias Delanteras.",
    #     "[2] Luminarias Traseras.",
    #     "[3] Hornillo y Toma Disponible vAC.",
    #     "[4] Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible).",
    #     "[5] Todas las luminarias.",
    #     "[6] Todo el sistema de Potencia.",
    #     "[7] Todo el sistema de Conmutacion."
    # ]
    # model = st.sidebar.selectbox("¿Que salida quiere conmutar?",options)
    

    st.title("Componentes Operativos de la Maquina de Niebla Salina")
    annotated_text(
    "En la anterior tabla podemos observar el estado en que se encuentran los diferentes componentes operativos de la Maquina de Niebla Salina. El estado comprendido como "
    ,":green[[1] = Encendido.]"
    , " y el estado "
    ,":red[[0] = Apagado.]"
    )
    df_conmu = input_params()
    st.table(df_conmu)

    st.sidebar.text("Software Desing by RuisoArt.")

    