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
            "Ⓒ All rights reserved 2023 -  built by Wilfred Hass, a UBC MDS program student"

        ]
    )
)