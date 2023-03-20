from dashboard.index import app
from dash import html, dcc
import dash_bootstrap_components as dbc

home_structure = html.Div(
    children=dbc.Container(
        [
            html.Br(),
            html.H2("Overview of the App",
                    style={"color": "black"}),
            html.Br(),
            dbc.Row(
                [
                    dcc.Markdown(
                        """
                        The purpose of this visualization dashboard is to present the best F1 drivers
                        out there and visualize how teams and drivers are doing in the last few years.
                        We can use it for exploratory data analysis (EDA) and to predict how teams might do
                        in the future based on their historical data. The primary objective of the dashboard
                        is to summarize how many races the top drivers have won, the position of the team's top driver or the top drivers in general
                        over time and finally comparing the drivers from
                        any two teams. This will allow users to gain a comprehensive understanding of current
                        F1 teams and identify how teams and drivers are performing over time.
                        From this information, we can further understand the winning teams and which team we might want to cheer for.
                        This might also serve for potential F1 new fans to get a view of
                        the competitive landscape and break the difficult barrier to entry into the sport.
                        """,
                        style={"color": "black"}),
                    dcc.Markdown(
                        """
                        This dashboard contains 3 visualisation tabs for your convenience!
                        >
                        >   * `Driver Race Wins`: This section shows a stacked bar chart with the total bar size showing how many races a specific
                        >   driver has won, with different colours representing differen teams that they've raced for. It features a with a multi-select
                        >   dropdown, allowing the user to choose which teams to display. The y-axis is the driver with the x-axis as the number of wins.
                        >   * `Position Over Time`: This section shows a timeplot of the team's position over multiple years to show how that team
                        >   is doing. Only the top driver from that year and that team is plotted to keep things concise. The radio items allow the 
                        >   user to choose if they want to look at the top 5 drivers with the highest number of points accumulated or the top 5 teams
                        >   that have accumulated the most points and how their top driver's position changed over time.
                        >   * `Comparing Points from Two Teams`: This bar chart shows the points earned by the top drivers of two selected (by single dropdown) teams.
                        >   The y-axis will show the drivers and the x-axis shows the number of points earned for that team.
                        >
                        Users can switch between tabs to compare the different metrics of teams/drivers.
                        """,
                        style={"color": "black"})
                ]
            ),
        ],
        fluid=True
    )
)