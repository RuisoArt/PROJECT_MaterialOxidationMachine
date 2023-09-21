"""
pip install random
pip install dash
pip install pandas
pip install plotly
"""
# reference: https://www.youtube.com/watch?v=N9yHClPGWG4&ab_channel=PabloPaniagua

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

route = "code\dashboard_test_two\data.csv"
df = pd.read_csv(route, delimiter = ';')

#Crear una tabla dinámica
pv = pd.pivot_table(df, 
                    index=['Name'], 
                    columns=["Status"], 
                    values=['Quantity'], 
                    aggfunc=sum, 
                    fill_value=0)

# Equivalente a excel a crear series
trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declinada')], name='Declinada')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pendiente')], name='Pendiente')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presentada')], name='Presentada')
trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'ganada')], name='Ganada')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Reporte de Funnel de Ventas'),
    html.Div(children='''Reporte Nacional de Ventas.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(title='Estado de orden por cliente', barmode='stack')
        })
])


if __name__ == '__main__':
    app.run_server(debug=True)
