from tkinter import *
import tkinter as tk

from code_body import notices_control as ntc
from code_config import comprobate_number as cbrint
from code_gpio import output_7_seven as out7
from code_config import window_alert as alt

def get_my_variables(window, hour_var, min_var):
    h_var = hour_var.get() #ya que estoy trabajando con entrys
    m_var = min_var.get()

    rh_var = cbrint.comprovate(h_var)
    rm_var = cbrint.comprovate(m_var)

    if rm_var == False or rh_var == False:
        print("Alguno de los numeros ingresados no son admisibles o no son numeros")
        #alerta de entrada no valida
        alt.my_alert_window()
    else:
        print("comprobar rango de hora")
        rrh_var = cbrint.range_hour(rh_var)
        #si hay hora y hay que verificar su rango
        print("comprobar rango de minute")
        rrm_var = cbrint.range_minute(rm_var)
        #si hay minuto y hay que verificar su rango
    
    if rrm_var == False or rrh_var == False:
        print("Alguno de los numeros ingresados no son admisibles o no son numeros")
        #alerta de entrada no valida
        alt.my_alert_window()
    else:
        out7.output_on(7)
        #ejecuta la maquina
        ntc.button_start(window, rrh_var, rrm_var)




# def get_my_variables(window, variable_entry):
#     var = variable_entry.get()

#     result = cbrint.comprovate(var)

#     if result == "yes":
#         seg = float(var) * 60
#         ntc.button_start(window, var, seg)
        
#     else:
#         print("No se encendio por el metodo START")


