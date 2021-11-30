# email: ehc0619@gmail.com
# password: marcoreus11
# user_id: 1892301

import requests
import json
import pandas as pd
from datetime import datetime, timedelta


# def lambda_handler(event, context):
#     email = "your_email"
#     password = "your_password"
#     user_id = "your_user_id"
#     update_team(email, password,user_id)

def get(url):
    response = requests.get(url)
    return json.loads(response.content)

def get_data():
    players =  get('https://fantasy.premierleague.com/api/bootstrap-static/')
    players_df = pd.DataFrame(players['elements'])
    teams_df = pd.DataFrame(players['teams'])
    events_df = pd.DataFrame(players['events'])