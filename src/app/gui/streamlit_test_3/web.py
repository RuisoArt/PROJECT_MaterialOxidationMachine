import streamlit as st
from PIL import Image as img
import pandas as pd
import pickle

route = './'
image = img.open(route+'img/machine.jpg')

def my_main():
    # https://docs.streamlit.io/library/api-reference/text/st.title
    st.title('Maquina de Niebla Salina'+
             '\n :new_moon: :waxing_crescent_moon: :first_quarter_moon: :moon: :waxing_gibbous_moon: :full_moon: 	:waning_gibbous_moon: :last_quarter_moon: :waning_crescent_moon: :new_moon:'+
             '\n :blue[by RuisoArt Project]')
    
    st.sidebar.header('Project Menu')

    st.image(image, caption='Simulacion 3D Maquina de Niebla Salina')


