# F1-DASHboard Proposal

## Purpose and Motivation

The purpose of this dashboard is to present Formula 1 racing data for exploratory data analysis (EDA) and predictive purposes. The primary objective is to summarize which teams have won the most races, how have teams or drivers performed in the recent past and to compare the top racers of two teams. This allows the user of the app to identify strong competitors, find out which teams are doing well and how a team might perform in the upcoming season.

The target audience is a new fan of Formula 1 racing, who might have some questions about which teams are good and which teams are underdogs. This person is looking to find out historical facts about teams, develop an intuition about the sport and easily answer any descriptive questions they might have as they watch the races or interviews.

Our role as this app's developer and data scientist, is to provide an understanding of the sport that I wish I had when I first got into the sport. Back then, I had wanted a way to interact with the data, so I could spend less time googling team statistics and more time watching the races!

## Data Description

The data used is from [kaggle](https://www.kaggle.com/datasets/tusharsingh1411/formula1-data-1950-2022), which is comprised of 3 datasets. Only 2 were used for the purpose of this app, with the important columns being:

- `Team`: The team of the driver
- `Driver`: The driver
- `Date`: The year of that season
- `PTS`: The points for that driver at the end of the season
- `Pos`: Position of the driver after the end of the season

We also create summary statistics as part of the visualizations:

- `Number of races won per driver`
- `Total number of points per driver`

There were other variables included in the dataset, but not used. Through some EDA, we found that there were no missing values, with 1618 rows for the file containing the details of each race and 1082 rows for the file containing the details of each season. This dataset includes these variables for the F1 seasons between 1950 and 2022. Since the dataset is fairly simple, EDA is not included in a separate file as most of the summary statistics can be found and verified on the Kaggle link above.

One thing to note is that as the sport evolved, rules changed and drivers can now earn more points/win more races in a season today versus drivers in the 1950s. Thus, much of the data exploration will be biased towards recent drivers, which is fine for our use case, as our target audience is more interested in recent years versus ones that occurred 70 years ago.

## Research Questions and Usage Scenarios

Lorenzo is a new fan of Formula 1, who recently learned about the sport from the Netlfix documentary series, "Drive to Survive". He has watched one season but is very interested in seeing a race. The local pub hosts watch parties and he wants to attend but doesn't want to seem like a complete newbie with the already experienced crowd that plans on going. In an attempt to learn more about the history, he starts the second season of the series, but is left with questions when the narrators reflect back to previous racing seasons. He ends up having to pause every 5 minutes to search for some statistics on the internet such as:

- Who has won the most races in F1 history?
- How has Ferrari performed over the last 10 years?
- Which team has the better drivers? Mercedes or Ferrari?

Instead of scouring the Internet, he instead finds this app and easily answers all of these questions quickly and efficiently! He navigates to the first tab and selects all of the teams from the dropdown, finding that Lewis Hamilton has won the most races. Then, he navigates to the second tab and selects the radio item for teams, showing how Ferrari has maintained a driver in the top 10 positions in the last 10 years. To answer his last question, he puts Mercedes and Ferrari head to head in the third tab, where he find that Lewis Hamilton drives for Mercedes, and has racked up an incredible amount of points over the years; more than the top 2 Ferrari drivers combined! He is able to finish the season of "Drive to Survive" before the F1 race watch party and he ends up impressing all of his friends with his newly found knowledge.
