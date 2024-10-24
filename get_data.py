
from os import environ as ENV
from json import dump

import requests as req
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.opendota.com/api"

if __name__ == "__main__":

    res = req.get(f"{BASE_URL}/players/{ENV['PLAYER_ID']}/matches")

    data = res.json()

    print(len(data))
    with open("tristan.json", "w") as f:
        dump(data, f, indent=6)
