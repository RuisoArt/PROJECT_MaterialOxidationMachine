import streamlit as st
from PIL import Image as img
import pandas as pd
import numpy as np
import pickle
#from my_time import this_my_local_time as time
from my_date import this_my_local_date as date
import datetime
import time
from sidebar_example import my_sidebar as mysd
from sidebar_example_1 import my_sidebar as mysdi

route = './'
image = img.open(route+'img/machine.jpg')

def this_my_local_time():
    aja = datetime.datetime.now()

    hour = str(aja.hour)
    minute = str(aja.minute)
    seconds = str(aja.second)

    my_date = hour+' : '+minute+' : '+seconds

    return my_date

def my_main():
    # https://docs.streamlit.io/library/api-reference/text/st.title
    st.title('Maquina de Niebla Salina'+
             '\n :new_moon: :waxing_crescent_moon: :first_quarter_moon: :moon: :waxing_gibbous_moon: :full_moon: 	:waning_gibbous_moon: :last_quarter_moon: :waning_crescent_moon: :new_moon:'+
             '\n :blue[by RuisoArt Project]')
    
    st.sidebar.header('Project Menu')
    
    my_time = this_my_local_time()
    st.subheader(str(':red[Local Time]: '+':orange[Date]: '+str(date)+' :violet[Time]: '+str(my_time)))

    # https://es.lipsum.com/
    st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
            "\n incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            "\n nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            "\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
            "\n fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "\n culpa qui officia deserunt mollit anim id est laborum.")
    
    st.subheader('Sensor de Temperatura 1: :orange[TermocuplaXXX]: ')
    mysd()
    st.subheader('Sensor de Temperatura 2: :orange[TermocuplaXXX]: ')
    mysdi()

    st.image(image, caption='Simulacion 3D Maquina de Niebla Salina')


