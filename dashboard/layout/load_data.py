import pandas as pd

def load_races():
    races = pd.read_csv("data/GrandPrix_races_details_1950_to_2022.csv", parse_dates=["Date", "Time", "year"], encoding='latin-1')
    return races

def load_laps():
    laps = pd.read_csv("data/GrandPrix_fastest-laps_details_1950_to_2022.csv", parse_dates=["Time", "year"])
    return laps

def load_drivers():
    drivers = pd.read_csv("data/GrandPrix_drivers_details_1950_to_2022.csv", parse_dates=["year"] )
    return drivers

# def load_data():
    
#     # Read data
#     drivers = pd.read_csv("data/GrandPrix_drivers_details_1950_to_2022.csv", parse_dates=["year"] )
#     laps = pd.read_csv("data/GrandPrix_fastest-laps_details_1950_to_2022.csv", parse_dates=["Time", "year"])
#     races = pd.read_csv("data/GrandPrix_races_details_1950_to_2022.csv", parse_dates=["Date", "Time", "year"], encoding='latin-1')
#     # constructors = pd.read_csv("data/constructors_championship_1958-2020.csv", parse_dates=["Year"])

#     # Rename some columns
#     laps.rename(columns={'Time': 'fastest_lap_time',
#                          'Car': 'fastest_lap_car',
#                          'Driver': 'fastest_driver'},
#                 inplace=True)
#     races.rename(columns={'Time': 'total_time',
#                           'Car': 'winner_car'},
#                  inplace=True)
#     # constructors.rename(columns={'Year': 'year'},
#     #              inplace=True)
    
#     full_df = laps.merge(races, on=["year", "Grand Prix"], how='left')
#     full_df = full_df.merge(drivers, on =["year"], how='left')
#     # full_df = full_df.merge(constructors, on=["year"], how='inner')
#     full_df.drop("year", axis=1, inplace=True)

#     return full_df