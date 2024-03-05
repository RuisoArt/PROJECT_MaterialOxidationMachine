import quandl
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
app = dash.Dash()
 
app.layout = html.Div(children=[
  html.Div(children='''BTC/Eur:'''),
  dcc.Input(id='input', value='', type='text'),
  html.Div(id='output-graph'),
])
 
@app.callback(
  Output(component_id='output-graph', component_property='children'),
  [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
  mydata =quandl.get("BITFINEX/BTCEUR", start_date="2017-5-5", end_date="2018-3-3")
 
  return dcc.Graph(
    id='example-graph',
    figure={
      'data': [
        {'x': mydata.index, 'y': mydata.High, 'type': 'line', 'name': input_data},
      ],
      'layout': {
        'title': input_data
      }
    }
  )
 
if __name__ == '__main__':
  app.run_server(debug=True)