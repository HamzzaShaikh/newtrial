import requests
import json

def apiCall():
    key = "?key=632ab6609b2c46318cfe9084af15c543"
    teams = requests.get("https://api.sportsdata.io/v3/nfl/scores/json/Teams" + key).json()
    teamNames = {}
    for dict in teams:
        tN = dict["Name"]
        keyTeam = dict["Key"]
        if tN not in teamNames:
            teamNames[keyTeam] = {"TeamName":tN, "Players":[]}
    # print(teamNames, len(teamNames))

    playerInfo = {}

    teamPlayers = requests.get("https://api.sportsdata.io/v3/nfl/scores/json/Players" + key).json()
    for dict in teamPlayers:
        if dict["Status"] == 'Active':
            teamNames[dict["CurrentTeam"]]["Players"].append(dict["PlayerID"])
            playerInfo[dict["PlayerID"]] = [dict["Name"], dict["CurrentTeam"],dict["Position"], dict["Height"], dict["Weight"], dict["BirthDate"], dict["College"]]

    return teamNames, playerInfo

# print(teamNames)
# print(playerInfo)

