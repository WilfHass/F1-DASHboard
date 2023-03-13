from dash import Dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://bootswatch.com/5/morph/bootstrap.css']
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)
app_title = "F1-DASHboard"
app.title = app_title