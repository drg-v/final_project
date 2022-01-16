import pickle
import os
import pandas as pd

from service import user_service, match_service, team_service

teams_convert = {
    'Man City': 0,
    'Liverpool': 1,
    'Chelsea': 2,
    'West Ham': 3,
    'Man United': 4,
    'Arsenal': 5,
    'Tottenham': 6,
    'Leicester': 7,
    'Wolves': 8,
    'Brentford': 9,
    'Brighton': 10,
    'Crystal Palace': 11,
    'Aston Villa': 12,
    'Everton': 13,
    'Leeds': 14,
    'Southampton': 15,
    'Watford': 16,
    'Burnley': 17,
    'Newcastle': 18,
    'Norwich': 19,
}


def get_prediction(match_id):
    match = match_service.get_match(match_id)
    if not match:
        return "fail"
    home, away = match.teams
    filename = '/finalized_model.sav'
    model = pickle.load(open('static' + filename, 'rb'))
    data = {'Home': [teams_convert[home.name]],
            'Away': [teams_convert[away.name]],
            'Home_goals_for': [home.goals_for],
            'Away_goals_for': [away.goals_for],
            'Home_goalsAgainst': [home.goals_against],
            'Away_goalsAgainst': [away.goals_against],
            'Home_wins': [home.wins],
            'Away_wins': [away.wins],
            'Home_losses': [home.losses],
            'Away_losses': [away.losses],
            'Home_value': [home.value],
            'Away_value': [away.value],
            'Home_points': [home.points],
            'Away_points': [away.points]}
    print("data:  ", data)
    df = pd.DataFrame(data)
    print(df)
    return model.predict(df)
