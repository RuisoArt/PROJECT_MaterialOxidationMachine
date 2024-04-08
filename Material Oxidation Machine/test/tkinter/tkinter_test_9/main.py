# aqui sera la interfaz principal que ejecutara por boton en pantalla alguna de las 2 a 3 interfaces que se utilizaran 
from .Code import control_dash
from .Context import register_dash
from .Database import read_MCU
from .Animation import animation_dash
"""
pip install pyinstaller
sudo apt-get install bcc
sudo apt-get install python-devel
pip3 install pyinstaller
pyinstaller --version


ruta de control dash

/home/onruiso/Desktop/Software/tkinter_test_9/Code/control_dash.py

ruta de register dash

/home/onruiso/Desktop/Software/tkinter_test_9/Context/register_dash.py

pyinstaller --windowed --onefile --icon=/home/onruiso/Desktop/Software/tkinter_test_9/ejecutable/icono/USTAcarpeta.ico /home/onruiso/Desktop/Software/tkinter_test_9/Code/control_dash.py

"""
