import streamlit as st
import pandas as pd

from params_response import my_user_response

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

    my_user_response(var1, var2, var3, var4, var5, var6, var7)

    return features