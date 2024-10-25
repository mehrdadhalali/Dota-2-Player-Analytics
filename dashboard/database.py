"""This script is for getting data from the database."""

from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor


def get_connection() -> connection:
    """Returns a live DB connection."""

    return connect(
        dbname="dota",
        cursor_factory=RealDictCursor
    )


def get_all_games_data():
    """Returns all of the games data from the database."""

    conn = get_connection()

    with conn.cursor() as curs:
        curs.execute(
            "SELECT * FROM game JOIN hero USING (hero_id) JOIN game_mode USING (game_mode_id);")
        data = curs.fetchall()
    conn.close()
    return data


def get_player_data():
    """Returns player data."""

    conn = get_connection()

    with conn.cursor() as curs:
        curs.execute(
            "SELECT * FROM player_details;")
        data = curs.fetchall()
    conn.close()
    return data
