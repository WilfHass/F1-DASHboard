from dashboard.index import app
from dashboard.layout.callbacks import callback
# from dashboard.layout.callbacks import pos_time_callback
# from dashboard.layout.load_data import load_races
from dashboard.layout.header import header, footer
import dash_bootstrap_components as dbc
# from dashboard.layout.racer_wins_tab import racer_wins_structure
from dash import (
    html,
    dcc
)

tabs = dbc.Container(
    [
        dcc.Tabs(
            id="app-tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Driver Race Wins", value="tab-1"),
                dcc.Tab(label="Position Over Time", value="tab-2"),
                dcc.Tab(label="Compare Points from Two Teams", value="tab-3"),
            ])
    ],
    fluid=True)
tabs_content = dbc.Container(id="tabs-content",
                        style={'float': 'top',
                               'width': '90%'},
                        className="main-panel",
        fluid=True)

app.layout = html.Div(
    [
        header,
        tabs,
        tabs_content,
        # footer
    ]
)
