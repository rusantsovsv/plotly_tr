import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6('Измени значение в чекбоксе чтобы увидеть функцию обратного вызова в действии'),
    html.Div([
        'Ввод: ',
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    
    html.Br(),
    html.Div(id='my-output', children='Hello'),
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')])
def update_output_value(input_value):
    return 'Вывод: {}'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)