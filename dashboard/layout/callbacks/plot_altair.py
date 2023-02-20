### Import Packages ###
from dashboard.index import app
from dashboard.layout.load_data import load_data
# from dashboard.layout.tab_2 import tab_2
from dash import (
    html,
    dcc,
    Input,
    Output
    )
import altair as alt

data = load_data("")
### Page 1 Layout and Callback ###
layout = html.Div(
    children=[
        html.H1(
            children='Scatter Plots',
        ),  
        html.Iframe(
            id='scatter',
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Dropdown(
            id='xcol-widget',
            value='Horsepower',  # REQUIRED to show the plot on the first page load
            options=[{'label': col, 'value': col} for col in data.columns]),
        html.Div(
            id='page-1-content',
        ),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ]
)

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(data).mark_point().encode(
        x=xcol,
        y='Displacement',
        tooltip='Horsepower').interactive()
    return chart.to_html()