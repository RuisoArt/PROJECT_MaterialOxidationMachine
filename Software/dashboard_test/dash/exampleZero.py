import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
  html.H1(children='HELLO WORLD'),
  dcc.Graph()])


if __name__ == '__main__':
 app.run_server(debug=True)

