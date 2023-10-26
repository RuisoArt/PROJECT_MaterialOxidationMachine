import streamlit as st
import pandas as pd

from annotated_text import annotated_text


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

    def input_params():
        var1 = st.sidebar.slider('[1] Luminarias Delanteras.', 0,1,0)
        var2 = st.sidebar.slider('[2] Luminarias Traseras.', 0,1,0)
        var3 = st.sidebar.slider('[3] Hornillo y Toma Disponible vAC.', 0,1,0)
        var4 = st.sidebar.slider('[4] Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible).', 0,1,0)
        var5 = st.sidebar.slider('[5] Todas las luminarias.', 0,1,0)
        var6 = st.sidebar.slider('[6] Todo el sistema de Potencia.', 0,1,0)
        var7 = st.sidebar.slider('[7] Todo el sistema de Conmutacion.', 0,1,0)

        if   var1 == 1:
            st.success("Luminarias delanteras Encendidas", icon="✅")
        elif var2 == 1:
            st.success("Luminarias Traseras Encendidas", icon="✅")
        elif var3 == 1:
            st.success("Hornillo Encendidas & Toma Disponible vAC Encendida", icon="✅")
        elif var4 == 1:
            st.success("Compresor de Aire & Sistema de Neblina Acida", icon="✅")
        elif var5 == 1:
            st.success("Todas las luminarias", icon="✅")
        elif var6 == 1:
            st.success("Todo el sistema de Potencia", icon="✅")
        elif var7 == 1:
            st.success("Todo el sistema de Conmutacion", icon="✅")
        
        elif var1 == 0:
            st.success("Luminarias delanteras Apagado", icon="❌")
        elif var2 == 0:
            st.success("Luminarias Traseras Apagado", icon="❌")
        elif var3 == 0:
            st.success("Hornillo Apagado & Toma Disponible vAC Apagado", icon="❌")
        elif var4 == 0:
            st.success("Compresor de Aire Apagado & Sistema de Neblina Acida Apagado", icon="❌")
        elif var5 == 0:
            st.success("Todas las luminarias Apagadas", icon="❌")
        elif var6 == 0:
            st.success("Todo el sistema de Potencia Apagado", icon="❌")
        elif var7 == 0:
            st.success("Todo el sistema de Conmutacion Apagado", icon="❌")
        else:
            print("ver data")
        

        data = {
            'Luminarias Delanteras':        var1,
            'Luminarias Traseras':          var2,
            'Hornillo & Toma Disponible':   var3,
            'Compresor & Nebulizador':      var4,
            'Todas luminarias':             var5,
            'Todo Sistema de Potencia':     var6,
            'Todo el Sistema':              var7
        }

        features = pd.DataFrame(data, index=[0])

        return features
    
    

    st.title("Componentes Operativos de la Maquina de Niebla Salina")
    annotated_text(
    "En la anterior tabla podemos observar el estado en que se encuentran los diferentes componentes operativos de la Maquina de Niebla Salina. El estado comprendido como "
    ,":green[[1] = Encendido.]"
    , " y el estado "
    ,":red[[0] = Apagado.]"
    )
    df_conmu = input_params()
    st.table(df_conmu)
    
    
    #................................................................................................

    st.sidebar.text("Software Desing by RuisoArt.")

    