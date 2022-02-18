#import packages
from matplotlib.pyplot import figure
import pandas as pd
import dash
import plotly.express as px
from dash import html
from dash import dcc


# read data in andas DataFrame
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding="ISO-8859-1", dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str})


# select random 500 datapoint from the data. setting random state to 35 so that we get same results.
data = airline_data.sample(n=500, random_state=35)

# display pie chart

fig = px.pie(data, values='Flights', names='DistanceGroup',
             title='Distance group proportion by flights')


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Airline Dashboard', style={
            'textAlign': 'center', 'color': '#503D36', 'font-size': 50}),
    html.P('Proportion of distance group (250 mile distance interval group) by flights.',
           style={'textAlign': 'center', 'color': '#F57241'}),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port='8000', debug=True)
