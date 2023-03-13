from dashboard.index import app
from dashboard.layout.load_data import load_drivers
from dash import html, dcc, dash, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash.exceptions import PreventUpdate
import pandas as pd

data = load_drivers()
print(data["Car"][1])
# top_10_winners = data.groupby('Driver'
#                               ).count().sort_values('Car',
#                                                     ascending=False).index[:10]
# winner_mask = data["Driver"].isin(top_10_winners)
# winner_teams = data[winner_mask].loc[:, "Car"].unique()

team_racer_points_structure = html.Div(
    children=dbc.Container(
        [
            html.Br(),
            html.H2("Put the Best Racers from 2 Teams Head-to-Head"),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id="team-racer-points-graph",
                            ),
                        ],
                        width={"size": 10},
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                html.Div(
                                    [
                                        "Team 1 Dropdown",
                                        dcc.Dropdown(
                                            options=data["Car"].unique(),
                                            value=data["Car"][0],
                                            id="team-1-compare",
                                            multi=False,
                                        ),
                                    ]
                                ),
                                fluid=True,
                            ),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Container(
                                html.Div(
                                    [
                                        "Team 2 Dropdown",
                                        dcc.Dropdown(
                                            options=data["Car"].unique(),
                                            value=data["Car"][1],
                                            id="team-2-compare",
                                            multi=False,
                                        ),
                                    ]
                                ),
                                fluid=True,
                            ),
                        ],
                        width={"size": 2, "float": "right"},
                    ),
                ]
            ),
        ],
        fluid=True
    )
)


# Set up callbacks/backend
@app.callback(
    Output("team-racer-points-graph", "figure"),
    Input("team-1-compare", "value"),
    Input("team-2-compare", "value"),
)
def update_team_racer_pts_graph(team1_compare, team2_compare):
    # Teams to include
    team1 = data.query(f"Car == '{team1_compare}'")
    # team1 = data[mask]

    team2 = data.query(f"Car == '{team2_compare}'")
    # team2 = data[mask]

    # Get top 5 drivers for each team
    team1_5 = team1.groupby("Driver").sum("PTS").sort_values("PTS", ascending=False)[:5]
    team1_5 = team1_5.sort_values("PTS", ascending=True)

    team2_5 = team2.groupby("Driver").sum("PTS").sort_values("PTS", ascending=False)[:5]
    team2_5 = team2_5.sort_values("PTS", ascending=True)

    fig = make_subplots(
        rows=2, cols=1, x_title="Points", y_title="Drivers", shared_xaxes=True
    )

    fig.add_trace(
        go.Bar(x=team1_5["PTS"], y=team1_5.index, orientation="h"), row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=team2_5["PTS"], y=team2_5.index, orientation="h"), row=2, col=1
    )

    fig.update_layout(bargap=0.2)
    # fig.update_annotations(x=-0.15, borderwidth=0, font_size=18, selector={'text': 'Drivers'})
    # fig.update_annotations(x=-0.1, selector={'text': f'{team1_compare}'})
    # fig.update_annotations(x=-0.1, selector={'text': f'{team2_compare}'})
    fig.update_layout(showlegend=False)
    fig.update_layout(
        margin=dict(l=150, r=10, t=60, b=80),
        paper_bgcolor="LightSteelBlue",
    )
    fig.update_yaxes(title_text=f"{team1_compare}", row=1, col=1)
    fig.update_yaxes(title_text=f"{team2_compare}", row=2, col=1)

    return fig


options = [{"label": team, "value": team} for team in data["Car"].unique()]


# Update dropdown 1
@app.callback(
    Output("team-1-compare", "options"),
    Input("team-1-compare", "search_value"),
    State("team-1-compare", "value"),
)
def update_d1_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.

    d1 = [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]
    return d1


# Update team 2 dropdown based on team 1
@app.callback(
    Output("team-2-compare", "options"),
    Input("team-1-compare", "search_value"),
    State("team-1-compare", "value"),
)
def update_d2_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    d1 = [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]
    return d1
