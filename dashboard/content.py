from dashboard.index import app
from dashboard.layout.racer_wins_tab import racer_wins_structure
from dashboard.layout.pos_time_tab import pos_time_structure
from dashboard.layout.team_racer_points_tab import team_racer_points_structure
from dashboard.layout.home_tab import home_structure
from dashboard.layout.header import header, footer
import dash_bootstrap_components as dbc
from dash import (
    Input,
    Output,
    html,
    dcc
)

tabs = dbc.Container(
    [
        dcc.Tabs(
            id="app-tabs",
            value="home-tab",
            children=[
                dcc.Tab(label="Overview", value="home-tab"),
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


@app.callback(Output("tabs-content", "children"),
              Input("app-tabs", "value"))
def callback(tab):
    if tab == "tab-1":
        return racer_wins_structure
    elif tab == "tab-2":
        return pos_time_structure
    elif tab == "tab-3":
        return team_racer_points_structure
    elif tab == "home-tab":
        return home_structure
    else:
        return html.H1('404')