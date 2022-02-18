# import libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


# read data in andas DataFrame
airline_data = pd.read_csv('airline_data.csv',
                           encoding="ISO-8859-1", dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Airline Performance Dashboard', style={
            'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Div(['Input Year  ', dcc.Input(id='input-year', value='2012', type='number',
             style={'height': '80px', 'font-size': 35}), ], style={'font-size': 40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id='line-plot')),
])


# adding callback decorator
@app.callback(Output(component_id='line-plot', component_property='figure'), Input(component_id='input-year', component_property='value'))
# callback function
def get_graph(entered_year):
    # Select data based on the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    #
    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=[
                    'ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time',
                      xaxis_title='Month', yaxis_title='ArrDelay')
    return fig


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8050', debug=True)
