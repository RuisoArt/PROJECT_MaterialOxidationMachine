import streamlit as st
from annotated_text import annotated_text
from web_params import input_params

def my_column():    
    st.sidebar.header("Menu de Conmutacion \n Salidas de Control ON / OFF \n Maquina de Niebla Salina.\n\n")   
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

    