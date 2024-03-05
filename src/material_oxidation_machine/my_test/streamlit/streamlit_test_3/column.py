import streamlit as st



def my_column():
    #var1, var2, var3, var4, var5, var6, var7 = 0,0,0,0,0,0,0 # hay que ver que no se reseteen cada que se ejecute OJO!
    var1, var2, var3, var4, var5, var6, var7 = "Apagado","Apagado","Apagado","Apagado","Apagado","Apagado","Apagado"
    #variables de conmutacion, estados
    st.sidebar.header("Menu de Conmutacion \n Salidas de Control ON / OFF \n Maquina de Niebla Salina.\n\n")

    options = [
        "[1] Luminarias Delanteras.",
        "[2] Luminarias Traseras.",
        "[3] Hornillo y Toma Disponible vAC.",
        "[4] Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible).",
        "[5] Todas las luminarias.",
        "[6] Todo el sistema de Potencia.",
        "[7] Todo el sistema de Conmutacion."
    ]
    model = st.sidebar.selectbox("¿Que salida quiere conmutar?",options)

    #................................................................................................
    if st.sidebar.button("ON"):
        if model == "[1] Luminarias Delanteras.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Luminarias delanteras Encendidas", icon="✅")
            var1 = "Encendido"

        elif model == "[2] Luminarias Traseras.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Luminarias Traseras Encendidas", icon="✅")
            var2 = "Encendido"

        elif model == "[3] Hornillo y Toma Disponible vAC.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Hornillo Encendidass \n Toma Disponible vAC Encendida", icon="✅")
            var3 = "Encendido"

        elif model == "[4] Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible).":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Compresor de Aire \n Sistema de Neblina Acida", icon="✅")
            var4 = "Encendido"

        elif model == "[5] Todas las luminarias.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todas las luminarias", icon="✅")
            var5 = "Encendido"

        elif model == "[6] Todo el sistema de Potencia.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todo el sistema de Potencia", icon="✅")
            var6 = "Encendido"

        elif model == "[7] Todo el sistema de Conmutacion.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todo el sistema de Conmutacion", icon="✅")
            var7 = "Encendido"

        else:
            print("Aqui se selecciono la opcion")
            st.sidebar.success("No se encendio Nada")
    #................................................................................................
    elif st.sidebar.button("OFF"):
        if model == "[1] Luminarias Delanteras.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Luminarias delanteras Apagado", icon="❌")
            var1 = "Apagado"

        elif model == "[2] Luminarias Traseras.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Luminarias Traseras Apagado", icon="❌")
            var2 = "Apagado"

        elif model == "[3] Hornillo y Toma Disponible vAC.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Hornillo Apagado \n Toma Disponible vAC Apagado", icon="❌")
            var3 = "Apagado"

        elif model == "[4] Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible).":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Compresor de Aire Apagado\n Sistema de Neblina Acida Apagado", icon="❌")
            var4 = "Apagado"

        elif model == "[5] Todas las luminarias.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todas las luminarias Apagado", icon="❌")
            var5 = "Apagado"

        elif model == "[6] Todo el sistema de Potencia.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todo el sistema de Potencia Apagado", icon="❌")
            var6 = "Apagado"

        elif model == "[7] Todo el sistema de Conmutacion.":
            print("Aqui se selecciono la opcion")
            st.sidebar.success("Todo el sistema de Conmutacion Apagado", icon="❌")
            var7 = "Apagado"

        else:
            print("Aqui se selecciono la opcion")
            st.sidebar.success("No se a apagado")
    #................................................................................................
    
    #................................................................................................

    st.sidebar.text("Software Desing by RuisoArt.")

    return var1, var2, var3, var4, var5, var6, var7