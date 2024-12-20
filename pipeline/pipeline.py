
from os import environ as ENV
from datetime import datetime

import requests as req
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor, execute_values

load_dotenv()

BASE_URL = "https://api.opendota.com/api"


def get_all_player_matches(player_id: int) -> list[dict]:
    """Returns all of the matches played by a player."""

    res = req.get(f"{BASE_URL}/players/{player_id}/matches?significant=0")

    data = res.json()
    return data


def get_player_details(player_id: int) -> dict:
    """Returns the player's details."""

    res = req.get(f"{BASE_URL}/players/{player_id}/")
    data = res.json()

    return {
        "name": data["profile"]["personaname"],
        "avatar_url": data["profile"]["avatarfull"]
    }


def get_connection() -> connection:
    """Returns a live DB connection."""

    return connect(
        dbname="dota",
        cursor_factory=RealDictCursor
    )


def clean_data(data: list[dict]) -> list[dict]:
    """Cleans the data of erroneous values."""

    data = [game for game in data
            if game["hero_id"] > 0]

    return data


def format_into_tuple(match: dict) -> tuple:
    """Formats the data of a single game into a tuple for insertion into the database."""

    game_id = match["match_id"]
    is_radiant = match["player_slot"] < 128
    radiant_won = match["radiant_win"]
    duration = match["duration"]
    time = datetime.fromtimestamp(match["start_time"])
    kills = match["kills"]
    deaths = match["deaths"]
    assists = match["assists"]
    hero_id = match["hero_id"]
    game_mode_id = match["game_mode"]

    return (game_id, is_radiant, radiant_won, duration,
            time, kills, deaths, assists,
            hero_id, game_mode_id)


def load_into_database(games: list[dict], player_details: dict):
    """Inserts data into the database."""

    conn = get_connection()
    to_insert = [format_into_tuple(game)
                 for game in games]
    query = """INSERT INTO game 
        (game_id, is_radiant, radiant_won, duration,
        time, kills, deaths, assists, hero_id,
        game_mode_id) VALUES %s;"""

    with conn.cursor() as curs:
        execute_values(curs, query, to_insert)

    with conn.cursor() as curs:
        curs.execute("""INSERT INTO player_details (detail_name, detail_value) VALUES
                     ('name', %s), ('image_url', %s);""", (player_details["name"],
                                                           player_details["avatar_url"]))
    conn.commit()
    conn.close()


if __name__ == "__main__":

    data = get_all_player_matches(ENV["PLAYER_ID"])
    player_data = get_player_details(ENV["PLAYER_ID"])

    load_into_database(clean_data(data), player_data)
