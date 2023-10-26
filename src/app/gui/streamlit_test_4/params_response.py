import streamlit as st

def my_user_response(var1, var2, var3, var4, var5, var6, var7):
    st.text("💠 Luminarias Delanteras : "                                               +('Encendido' if var1==1 else 'Apagado')+"\n"
            "💠 Luminarias Traseras : "                                                 +('Encendido' if var2==1 else 'Apagado')+"\n"
            "💠 Hornillo y Toma Disponible vAC : "                                      +('Encendido' if var3==1 else 'Apagado')+"\n"
            "💠 Compresor de Aire y Sistema de Neblina Acida(Resistor Sumerjible) : "   +('Encendido' if var4==1 else 'Apagado')+"\n"
            "💠 Todas las luminarias : "                                                +('Encendido' if var5==1 else 'Apagado')+"\n"
            "💠 Todo el sistema de Potencia : "                                         +('Encendido' if var6==1 else 'Apagado')+"\n"
            "💠 Todo el sistema de Conmutacion : "                                      +('Encendido' if var7==1 else 'Apagado')+"\n"
    )

    

