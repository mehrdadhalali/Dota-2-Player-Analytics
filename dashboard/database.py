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


def get_all_data():
    """Returns all of the data from the database."""

    conn = get_connection()

    with conn.cursor() as curs:
        curs.execute(
            "SELECT * FROM game JOIN hero USING (hero_id) JOIN game_mode USING (game_mode_id);")
        data = curs.fetchall()
    conn.close()
    return data
