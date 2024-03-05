# pip install pandas
# pip install --upgrade pip
# pip install streamlit
# pip install -U scikit-learn
# pip install matplotlib

# importar las librerias
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC

import pickle

# carga de datos en dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# separar los datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, Y)

#inicializar modelos de regresion linear, logistica y de supervectorC
lin_reg = LinearRegression()
log_reg = LogisticRegression()
svc_m = SVC()

#entrenar modelos
lin_regression = lin_reg.fit(x_train, y_train)
log_regression = log_reg.fit(x_train, y_train)
svc_model = svc_m.fit(x_train, y_train)

#guardar entrenamientos en archivo binario píckle, similar a un json
with open('./src/app/gui/streamlit_test_2/data/linear_regression.pkl', 'wb') as li:
    pickle.dump(lin_regression, li)

with open('./src/app/gui/streamlit_test_2/data/logistic_regression.pkl', 'wb') as lo:
    pickle.dump(log_regression, lo)

with open('./src/app/gui/streamlit_test_2/data/svc_model.pkl', 'wb') as sv:
    pickle.dump(svc_model, sv)