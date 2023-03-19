# F1-DASHboard

Team members: Wilfred Hass

## F1 Statistics

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

## About the Data

The data set presented and used in this project is adopted from the
[Formula 1](https://www.kaggle.com/datasets/tusharsingh1411/formula1-data-1950-2022)
data set on the Kaggle website. The data set comprises of the driver positions/points earned at the end
of each year (Grand Prix), the fastest lap for each race and corresponding driver/teams, and the results
of each race (winner, number of laps, location). A more in-depth explanation can be found in [the proposal](doocs/proposal.md).
data dictionary.

## Description of the Dashboard

This dashboard contains 3 visualisation tabs and one home tab:

- `Number of Races Won Based on Team`: This section shows a stacked bar chart with the total bar size showing how many races that driver has won. It features a with a multi-select dropdown, allowing the user to choose which teams to display. The y-axis is the driver with the x-axis as the number of wins.

- `Position of Team Over Time`: This section shows a timeplot of the team's position over multiple years to show how that team is doing. Only the top driver from that year and that team is plotted to keep things concise. The radio items allow the user to choose if they want to look at the top 5 drivers with the highest number of points accumulated or the top 5 teams that have accumulated the most points and how their top driver's position changed over time.

- `Comparing Drivers and Teams`: This bar chart shows the points earned by each driver of two selected (by single dropdown) teams. The y-axis will show the drivers and the x-axis shows the number of points earned for that team.

Users can switch between tabs to compare the different metrics of teams/drivers.

## Contribute!

Interested in contributing? Check out the [Contributing](CONTRIBUTING.md) guidelines. By contributing to this project, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

There is substantial room to continue development of the project. Currently, we only have 3 visualizations but there is so many different questions that can be answered with this dataset. If you have an idea, please let us know by opening an issue in the repository!

## Contributors

Team members: Wilfred Hass

<a href="https://github.com/wilfhass/F1-DASHboard/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wilfhass/F1-DASHboard&max=1000" />
</a>