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
            html.H2("Check how teams or drivers are doing over time"),
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
                                            "Time Series Selector",
                                            dcc.RadioItems(
                                                options={
                                                    "Driver": "Driver",
                                                    "Car": "Team",
                                                },
                                                value="Driver",
                                                id="col-team-driver",
                                                labelStyle={
                                                    "display": "flex",
                                                    "align-items": "center",
                                                },
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
        fluid=True,
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

    # Get top 5 drivers or teams in terms of points since 2010
    top_5 = (
        df.groupby(posCol)
        .sum(numeric_only=True)
        .sort_values("PTS", ascending=False)
        .index[:5]
    )

    mask = df[posCol].isin(top_5)
    df = df[mask]

    if posCol == "Car":
        # Get only top driver from those top teams
        df = df.loc[df.groupby(["year", posCol], sort=False)["Pos"].idxmin()]
        title = "Top Driver Positions From Each of the Top 5 Teams From 2010-2022"
        ylim = [10, 0.5]
    else:
        title = "Top Driver Positions From 2010-2022"
        ylim = [18, 0.5]

    fig = px.scatter(
        df,
        x="year",
        y="Pos",
        color=posCol,
        title=title,
        labels={"year": "Year", "Pos": "Position",
                "Winner": "Driver", "Car": "Team"},
    )
    for i in range(len(fig.data)):
        fig.data[i].update(mode="markers+lines")

    fig.update_layout(
        margin={"l": 40, "b": 50, "t": 40, "r": 20},
        paper_bgcolor="LightSteelBlue"
    )
    fig.update_yaxes(range=ylim)

    return fig
