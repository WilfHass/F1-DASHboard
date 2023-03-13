### Import Packages ###
from dashboard.index import app
from dashboard.layout.racer_wins_tab import racer_wins_structure
from dashboard.layout.pos_time_tab import pos_time_structure
from dashboard.layout.team_racer_points_tab import team_racer_points_structure
from dash import (
    Input,
    Output,
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
    else:
        return '404'