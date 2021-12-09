import requests

url = "https://free-epic-games.p.rapidapi.com/free"

headers = {
    'x-rapidapi-host': "free-epic-games.p.rapidapi.com",
    'x-rapidapi-key': "668e158525mshca6a72c60478528p15b9ccjsn7794ff41beea"
}


def stufn():
    response = requests.request("GET", url, headers=headers)
    return response.json()


def game():
    tog = []
    games = stufn()
    for n in range(3):
        joe = games['freeGames']['current'][n]['title']
        tog.append(joe)
    print(tog)
    return tog

