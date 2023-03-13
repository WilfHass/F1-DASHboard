from dashboard.index import app
from dashboard.layout.load_data import load_drivers
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd


data = load_drivers()

pos_time_structure = html.Div(
    children=dbc.Container(
        [
            html.Br(),
            html.H2("Check how teams/drivers are doing over time"),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(id="pos-time-graph")], width={"size": 10}),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    html.Div(
                                        [
                                            "Team or Winner Dropdown",
                                            dcc.Dropdown(
                                                options={
                                                    "Driver": "Driver",
                                                    "Car": "Team",
                                                },
                                                value="Driver",
                                                id="col-team-driver",
                                            ),
                                        ]
                                    ),
                                ],
                                fluid=True,
                            )
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
    Output("pos-time-graph", "figure"), Input("col-team-driver", "value")
)  # add year limiter
def update_pos_time_graph(posCol):
    # Include since year
    mask = data["year"] > pd.Timestamp(2010, 1, 1)
    df = data[mask]
    df.loc[:, "Pos"] = df.loc[:, "Pos"].astype(int)

    # Get top 10 drivers or teams
    top_5 = (
        data.groupby(posCol)
        .sum(numeric_only=True)
        .sort_values("PTS", ascending=False)
        .index[:5]
    )
    mask = df[posCol].isin(top_5)
    df = df[mask]

    fig = px.scatter(
        df,
        x="year",
        y="Pos",
        color=posCol,
        title="Position From 2010-2022",
        labels={"year": "Year", "Pos": "Position", "Winner": "Driver", "Car": "Team"},
    )
    for i in range(len(fig.data)):
        fig.data[i].update(mode="markers+lines")
    # fig.update_layout(bargap=0.2, xaxis_title="Number of Races Won",)
    fig.update_layout(
        margin={"l": 40, "b": 40, "t": 60, "r": 0},
        paper_bgcolor="LightSteelBlue",
    )

    return fig
