import streamlit as st
from PIL import Image as img

from sidebar_example import my_sidebar as mysd
from sidebar_example_1 import my_sidebar as mysdi

from web_column import my_column as myco
from web_localtime import my_localtime as mylocaltime
from web_image import image_3d_machine as machine_img
from params_response import my_user_response as res

def my_main():
    # https://docs.streamlit.io/library/api-reference/text/st.title
    st.title('Maquina de Niebla Salina'+
             '\n :new_moon: :waxing_crescent_moon: :first_quarter_moon: :moon: :waxing_gibbous_moon: :full_moon: 	:waning_gibbous_moon: :last_quarter_moon: :waning_crescent_moon: :new_moon:'+
             '\n :blue[by RuisoArt Project]')

    mylocaltime()

    # aqui se recive las variables que pareceran en la pantalla de si estan encendidas o apagadas
    myco()

    # https://es.lipsum.com/
    st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
            "\n incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis "
            "\n nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            "\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
            "\n fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "\n culpa qui officia deserunt mollit anim id est laborum.")
    
    image = machine_img()
    st.image(image, caption='Simulacion 3D Maquina de Niebla Salina')
   
    st.subheader('Sensor de Temperatura 1: :orange[TermocuplaXXX]: ')
    mysd()
    st.subheader('Sensor de Temperatura 2: :orange[TermocuplaXXX]: ')
    mysdi()

    

    


