import streamlit as st
import datetime

from my_date import this_my_local_date as mydate
from my_time import this_my_local_time as mytime

def my_localtime():
    st.subheader(':red[Local Time]: :orange[Date]:'+str(mydate)+':violet[Time]: '+str(mytime))

