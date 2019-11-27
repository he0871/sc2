"""
Description:fetch the match history via starcraft 2 community api
Author: Jingyuan He
Date: 11/24/2019
"""
import requests
import json

# import credential

url = "https://us.battle.net/oauth/token"

# payload = {
#     'grant_type': 'client_credentials',
#     'client_id': credential.client_id,
#     'client_secret': credential.client_secret,
# }

payload = {
    'grant_type': 'client_credentials',
    'client_id': 'a40d69d0e1554ff49e272d27a451790f',
    'client_secret': '6qtnPOmIEZpXRxw2ZWO8MzozpwkZfPG9',
}

response = requests.post(url, data=payload)
print(response.content)
print(response.text)
print(type(response.content))
res_dict = json.loads(response.content.decode('utf-8'))
print(res_dict)
print(res_dict["access_token"])
access_token = res_dict["access_token"]
print("match history")
requests_url = "https://us.api.blizzard.com/sc2/legacy/profile/1/1/10400261/matches"
Whole_url = requests_url + '?' + 'access_token=' + access_token
MatchHistory = requests.get(Whole_url)
print(MatchHistory)
# print(MatchHistory.content)
MH_dict = json.loads(MatchHistory.content.decode('utf-8'))
matches = MH_dict["matches"]
print(matches[0])
