"""This script is for seeding the database with metadata."""

import requests as req
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor, execute_values

BASE_URL = "https://api.opendota.com/api"


def get_connection() -> connection:
    """Returns a live DB connection."""

    return connect(
        dbname="dota",
        cursor_factory=RealDictCursor
    )


def get_metadata(conn: connection) -> dict:
    """Collects all of the metadata from the API."""

    hero_res = req.get(f"{BASE_URL}/heroes")
    game_mode_res = req.get(f"{BASE_URL}/constants/game_mode")

    return {
        "heroes": hero_res.json(),
        "game_modes": game_mode_res.json().values()
    }


def seed_heroes(hero_data: list[dict], conn: connection):
    """Seeds the heroes table."""

    to_insert = [(hero["id"], hero["localized_name"])
                 for hero in hero_data]
    query = "INSERT INTO hero (hero_id, hero_name) VALUES %s;"

    with conn.cursor() as curs:
        execute_values(curs, query, to_insert)


def seed_modes(game_modes: list[dict], conn: connection):
    """Seeds the heroes table."""

    to_insert = [(mode["id"], mode["name"])
                 for mode in game_modes]
    query = "INSERT INTO game_mode (game_mode_id, game_mode_name) VALUES %s;"

    with conn.cursor() as curs:
        execute_values(curs, query, to_insert)


if __name__ == "__main__":

    con = get_connection()
    data = get_metadata(con)
    seed_heroes(data["heroes"], con)
    seed_modes(data["game_modes"], con)
    con.commit()
    con.close()
