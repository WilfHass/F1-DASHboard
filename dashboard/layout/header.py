from dash import html
from dashboard.index import app
import dash_bootstrap_components as dbc

header = html.Header(
    dbc.Container(
        [
            html.Br(),
            html.H1('F1 DASHboard!'),
            html.Br(),
        ],
        fluid=True
    )
)

footer = html.Footer(
    dbc.Container(
        [
            html.Br(),
            'Created by Wilfred Hass'
        ]
    )
)