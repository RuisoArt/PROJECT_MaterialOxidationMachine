"""
Para instalar dash en Linux se utiliza el siguiente comando:

    sudo pip install dash dash-renderer dash-html-components dash-core-components plotly

Para instalarlo en Windows utilizamos el siguiente comando:

    pip install dash dash-renderer dash-html-components dash-core-components plotly
"""

#https://unipython.com/introduccion-dash-una-potente-guis-visualizadores-dinamicos/

# Las librerias son:
import dash
import dash_core_components as dcc
import dash_html_components as html

#inicializar aplicacion
app = dash.Dash() # aqui le decimos que nuestra app utilice Dash para trabajar.

# El id es obligatorio, pues con el podemos manipular despues el grafico
app.layout = html.Div(
    children=[
        html.H1('HELLO WORLD'),dcc.Graph(
            id="ejemplo", figure={
                'data':[
                    {'x': [1, 2, 3, 4], 'y': [1, 8, 3, 7], 'type': 'line', 'name': 'Bicicletas'},
                    {'x': [1, 2, 3, 4], 'y': [5, 2, 10, 8], 'type': 'bar', 'name': 'Bicicletas electricas'},
                ],'layout': {'title': 'Ejemplo básico en Dash'}
            })
        ]) #diseño base similar a flask

if __name__ == '__main__':
 app.run_server(debug=True)

 #tras un tiempo se puede cerrar la ejecucion continua, en este caso, hay que ir al administrador de tareas o procesos y configurar que procesos se quiere que se recargen solos o que no se reinicien nuevamente