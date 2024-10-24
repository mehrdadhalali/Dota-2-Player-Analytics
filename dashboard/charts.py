"""This script is for creating the charts."""

import pandas as pd
import altair as alt


def turn_into_dataframe(db_data: list[dict]) -> pd.DataFrame:
    """Turns the data from the database into a dataframe."""

    df = pd.DataFrame(db_data)
    df["won"] = ~(df["is_radiant"] ^ df["radiant_won"])

    return df


def create_hero_bar_chart(df: pd.DataFrame) -> alt.Chart:

    games_per_hero = df.groupby(["hero_name"]).count().reset_index()
    games_per_hero = games_per_hero.sort_values(
        by=["game_mode_id"], ascending=False)
    games_per_hero = games_per_hero[:10]

    hero_bar_chart = alt.Chart(games_per_hero).mark_bar().encode(
        x=alt.X("hero_name", title="Hero").sort("-y"),
        y=alt.Y("game_mode_id", title="Number of games")
    )

    return hero_bar_chart
