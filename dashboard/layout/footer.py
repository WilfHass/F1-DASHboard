# package imports
from dash import html
import dash_bootstrap_components as dbc

footer = html.Footer(
    dbc.Container(
        [
            html.Hr(),
            'Footer item 1',
            html.Br(),
            'Footer item 2',
            html.Br(),
            'Footer item 3'
        ]
    )
)