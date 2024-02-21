from tkinter import *
import tkinter as tk

from code_body import notices_control as ntc
from code_config import comprobate_number as cbrint
from code_gpio import output_7_seven as out7

def get_my_variables(window, variable_entry):
    var = variable_entry.get()

    result = cbrint.comprovate(var)

    if result == "yes":
        seg = float(var) * 60
        ntc.button_start(window, var, seg)
        out7.output_on(7)
    else:
        print("No se encendio por el metodo START")


