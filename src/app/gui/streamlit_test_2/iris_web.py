# importar librerias
import streamlit as st
import pickle
import pandas as pd

# para correr un proyecto de streamlit se utiliza el comando:
#   streamlit run proyect_name.py

# extraer los archivos pickle que creamos con iris_model.py
#route = './src/app/gui/streamlit_test_2/data/'
route = './data/'

with open(route+'linear_regression.pkl', 'rb') as li:
    lin_regression = pickle.load(li)

with open(route+'logistic_regression.pkl', 'rb') as lo:
    log_regression = pickle.load(lo)

with open(route+'svc_model.pkl', 'rb') as sv:
    sv_model = pickle.load(sv)

# funcion parea clasificar las plantas
"""
[0] = setoso
[1] = vercolor
[2] = virginica
"""
def classify(num):
    if num == 0:
        return 'Setosa'
    if num == 1:
        return 'Versicolor'
    if num == 2:
        return 'Virginica'
    else:
        return 'Nothing'
    
def main():
    st.title('Modelamiento de Iris')

    st.sidebar.header('Entrada de datos del Usuario')

    #funcion para poner los parametros del sidebar
    def user_imput_parameters():
        sepal_lenght = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_lenght = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)

        #un diccionario para utilizar la data
        data = {
            'sepal_length': sepal_lenght,
            'sepal_width': sepal_width,
            'petal_length': petal_lenght,
            'petal_width': petal_width
        }
        features = pd.DataFrame(data, index=[0])

        return features

    df = user_imput_parameters()
    
    # escoger el moelo a trabajar por el usuario
    options = ['Linear Regression', 'Logistic Regression', 'SVC']
    model = st.sidebar.selectbox("Con que modelo quieres trabajar?", options)

    st.subheader("Parametros de l Usuario")
    st.subheader(model)
    st.write(df)

    if st.button("RUN"):
        if model == "Linear Regression":
            st.success(classify(lin_regression.predict(df)))
        elif model == "Logistic Regression":
            st.success(classify(log_regression.predict(df)))
        elif model == "SVC":
            st.success(classify(sv_model.predict(df)))

# metodo de netrada al script
if __name__ == '__main__':
    main()
