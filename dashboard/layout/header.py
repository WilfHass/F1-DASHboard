from dash import html
import dash_bootstrap_components as dbc

header = html.Header(
    dbc.Container(
        [
            html.Hr(),
            'Header item 1'
        ]
    )
)