from dashboard.index import app
from dashboard.layout.load_data import load_races
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import pandas as pd

data = load_races()
top_10_winners = (
    data.groupby("Winner").count().sort_values("Car", ascending=False).index[:10]
)
winner_mask = data["Winner"].isin(top_10_winners)
winner_teams = data[winner_mask].loc[:, "Car"].unique()


racer_wins_structure = html.Div(
    children=dbc.Container(
        [
            html.Br(),
            html.H2("How Do Racers Compare?"),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id="crossfilter-racer-wins"
                                )
                        ],
                        width={"size": 8},
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                html.Div(
                                    [
                                        "Team Dropdown",
                                        dcc.Dropdown(
                                            options=data["Car"].unique(),
                                            value=winner_teams,
                                            id="crossfilter-team",
                                            multi=True,
                                        ),
                                    ]
                                ),
                                fluid=True,
                            )
                        ],
                        width={"size": 4, "float": "right"},
                    ),
                ]
            ),
        ],
        fluid=True,
    ),
    # style={'padding': '10px 5px'}
)


# Set up callbacks/backend
@app.callback(
    Output("crossfilter-racer-wins", "figure"), Input("crossfilter-team", "value")
)
def update_race_wins_graph(team_filter):
    # Teams to include
    mask = data["Car"].isin(team_filter)
    df = data[mask]

    # Get top 10 drivers
    top_10_drivers = (
        df.groupby("Winner").count().sort_values("Car", ascending=False).index[:10]
    )
    driver_mask = df["Winner"].isin(top_10_drivers)
    driver_df = df[driver_mask]
    # driver_df = driver_df.groupby("Winner").count().reset_index()

    fig = px.histogram(
        driver_df,
        y="Winner",
        color="Car",
        title="Number of Race Wins From 1950-2022",
        barmode="stack",
        labels={"year": "Number of Races Won", "Winner": "Driver", "Car": "Team"},
    )
    fig.update_layout(
        bargap=0.2,
        xaxis_title="Number of Races Won",
        yaxis={"categoryorder": "total ascending"},
    )
    fig.update_layout(
        margin={"l": 150, "b": 60, "t": 60, "r": 0},
        paper_bgcolor="LightSteelBlue",
    )

    return fig


options = [{"label": team, "value": team} for team in data["Car"].unique()]


@app.callback(
    Output("crossfilter-team", "options"),
    Input("crossfilter-team", "search_value"),
    State("crossfilter-team", "value"),
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]
