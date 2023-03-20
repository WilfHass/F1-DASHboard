from dashboard.index import app
from dashboard.layout.load_data import load_drivers
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = load_drivers()

team_racer_points_structure = html.Div(
    children=dbc.Container(
        [
            html.Br(),
            html.H2("Put the best drivers from 2 teams head-to-head"),
            html.Br(),
            dcc.Markdown(
              """
              In this bar chart, you may select two teams to compare their top 5 drivers. The bar chart shows how many points 
              each driver has earned over their career. 
              """  
            ),
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
                                            value="Ferrari",
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
                                            value="Mercedes",
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
        fluid=True,
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

    team2 = data.query(f"Car == '{team2_compare}'")

    # Get top 5 drivers for each team
    team1_5 = team1.groupby("Driver").sum("PTS").sort_values("PTS", ascending=False)[:5]
    team1_5 = team1_5.sort_values("PTS", ascending=True)

    team2_5 = team2.groupby("Driver").sum("PTS").sort_values("PTS", ascending=False)[:5]
    team2_5 = team2_5.sort_values("PTS", ascending=True)

    fig = make_subplots(
        rows=2, cols=1, x_title="Points", shared_xaxes=True
    )

    fig.add_trace(
        go.Bar(x=team1_5["PTS"], y=team1_5.index, orientation="h"), row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=team2_5["PTS"], y=team2_5.index, orientation="h"), row=2, col=1
    )

    fig.update_layout(bargap=0.2)
    fig.update_layout(showlegend=False)
    fig.update_layout(
        margin=dict(l=150, r=10, t=60, b=80),
        paper_bgcolor="LightSteelBlue",
    )
    fig.update_yaxes(title_text=f"{team1_compare} Drivers", row=1, col=1)
    fig.update_yaxes(title_text=f"{team2_compare} Drivers", row=2, col=1)

    return fig