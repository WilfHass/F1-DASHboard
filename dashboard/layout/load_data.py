import pandas as pd

def load_races():
    races = pd.read_csv("data/GrandPrix_races_details_1950_to_2022.csv", parse_dates=["Date", "Time", "year"], encoding='latin-1')
    races["Winner"] = races["Winner"].str.replace('\s+', ' ', regex=True)
    races["Car"] = races["Car"].str.replace('\s+', ' ', regex=True)
    return races

def load_drivers():
    drivers = pd.read_csv("data/GrandPrix_drivers_details_1950_to_2022.csv", parse_dates=["year"] )
    drivers["Driver"] = drivers["Driver"].str.replace('\s+', ' ', regex=True)
    drivers["Car"] = drivers["Car"].str.replace('\s+', ' ', regex=True)
    return drivers