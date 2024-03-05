import streamlit as st
from PIL import Image as img

def image_3d_machine():
    route = './'
    image = img.open(route+'img/machine.jpg')

    return image