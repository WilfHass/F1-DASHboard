# F1-DASHboard

Team members: Wilfred Hass

## F1 Statistics 

The purpose of this visualization dashboard is to present the best F1 drivers
out there and visualize how teams and drivers are doing in the last few years.
We can use it for exploratory data analysis (EDA) and predict how teams might do
in the future based on their historical data. The primary objective of the dashboard
is to summarize how many races the top drivers have won, the team or driver positions 
over time, how the team performs at each venue and finally comparing the drivers from 
any two teams. This will allow users to gain a comprehensive understanding of current
F1 teams and identify how teams and drivers are performing over time and location. 
From this information, we can make informed decisions on winning teams and which bandwagon
we might want to hop on. This might also serve for potential F1 newbies to get a view of
the competitive landscape and break the difficult barrier to entry into the sport. 

## About the Data

The data set presented and used in this project is adopted from the
[Formula 1](https://www.kaggle.com/datasets/tusharsingh1411/formula1-data-1950-2022)
data set on the Kaggle website. The data set comprises of the driver positions/points earned at the end
of each year (Grand Prix), the fastest lap for each race and corresponding driver/teams, and the results
of each race (winner, number of laps, location). A more in-depth explanation can be found in [the proposal](Proposal.md).
data dictionary.

## Description of the Dashboard

This dashboard contains 4 tabs, each showing a different visualisation:

-   `Number of Races Won Based on Team`: This section shows a stacked bar chart with the total showing how many races that driver has won, with a multi-select dropdown, allowing the user to choose which teams to display. The y-axis is the driver with the x-axis as the number of wins.
-   `Position of Team Over Time`: This section shows a timeplot of the team's position over multiple years to show how that team is doing. There is a multi-select dropdown to choose which teams you want to see the historical data for.
-   `Points Earned Based on Venue`: A stacked bar chart showing how may points a team has earned based on the venue selected. The y-axis shows the team and the x-axis shows the number of points. Hovering over a section of the bar shows the nuber of points earned by that venue. The multi-select dropdown shows the venues that you may want to compare.
-   `Comparing Drivers and Teams`: This bar chart shows the points earned by each driver of two selected (by dropdown) teams. The y-axis will show the drivers and the x-axis shows the number of points earned for that team.

Users can switch between tabs to compare the different metrics of teams/drivers.

## Sketch

![](img/sketch.png)
