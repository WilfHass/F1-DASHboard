from dashboard.index import app
from dashboard.layout.callbacks import plot_altair
from dashboard.layout.load_data import load_data
from dashboard.layout.header import header
from dashboard.layout.footer import footer
from dash import (
    html,
    dcc
)

# tabs = dcc.Tabs(
#     id="app-tabs",
#     value="tab-1",
#     children=[
#         dcc.Tab(label="Tab1", value="tab-1"),
#         dcc.Tab(label="Tab2", value="tab-2"),
#     ],
# )
# tabs_content = html.Div(id="tabs-example-content", className="main-panel")

data = load_data("")

### Page 1 Layout and Callback ###
scatter = html.Div(
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
    ]
)

app.layout = html.Div(
    [
        header,
        scatter,
        # tabs_content,
        footer
    ]
)