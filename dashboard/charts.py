"""This script is for creating the charts."""

import pandas as pd
import altair as alt


def turn_into_dataframe(db_data: list[dict]) -> pd.DataFrame:
    """Turns the data from the database into a dataframe."""

    df = pd.DataFrame(db_data)
    df["won"] = ~(df["is_radiant"] ^ df["radiant_won"])

    return df


def create_hero_bar_chart(df: pd.DataFrame) -> alt.Chart:

    games_per_hero = df["hero_name"].value_counts().reset_index()
    games_per_hero = games_per_hero[:10]
    top_10_heroes = games_per_hero["hero_name"].tolist()
    hero_wl = df.groupby(["hero_name", "won"]).size().reset_index()
    hero_wl = hero_wl[hero_wl["hero_name"].isin(top_10_heroes)]
    hero_wl.columns = ["hero_name", "won", "count"]

    hero_bar_chart = alt.Chart(hero_wl,
                               title=alt.Title("Most Played Heroes", color="#FFFFFF",
                                               anchor="middle")).mark_bar().encode(
        x=alt.X("hero_name", title="Hero").sort("-y"),
        y=alt.Y("count", title="Number of games"),
        color=alt.Color("won", scale=alt.Scale(range=['#ff0000', '#32CD32']))
    )

    return hero_bar_chart


def calculate_win_rate(df: pd.DataFrame) -> float:
    """Calculates player's win rate."""

    win_count = len(df[df["won"]])

    win_rate = win_count/(len(df))

    return round(win_rate*100, 2)


def calculate_averages(df: pd.DataFrame) -> tuple[float]:
    """Calculates average KDA."""

    av_kills = df["kills"].mean()
    av_deaths = df["deaths"].mean()
    av_assists = df["assists"].mean()

    return (av_kills, av_deaths, av_assists)
