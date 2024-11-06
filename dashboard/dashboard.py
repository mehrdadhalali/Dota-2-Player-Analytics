"""The dashboard"""

import streamlit as st

from charts import create_hero_bar_chart, turn_into_dataframe, calculate_win_rate, calculate_averages
from database import get_all_games_data, get_player_data

st.set_page_config(layout="wide")

if __name__ == "__main__":

    db_data = get_all_games_data()
    player_data = get_player_data()
    player_name = player_data[0]["detail_value"]
    player_avatar = player_data[1]["detail_value"]

    data = turn_into_dataframe(db_data)

    cols = st.columns([2, 0.5])
    with cols[0]:
        st.header(
            f"Welcome to your Dota 2 Analytics Dashboard, {player_name}.")
        sub_cols = st.columns([1, 1, 1])
        with sub_cols[0]:
            wr_text = f"Win Rate: {calculate_win_rate(data)}%"
            st.markdown(f"<h3 style='text-align: center'> {wr_text} </h3>",
                        unsafe_allow_html=True)

        with sub_cols[1]:
            av_kills, av_deaths, av_assists = calculate_averages(data)
            st.write(f"Average Kills: {round(av_kills, 2)}")
            st.write(f"Average Deaths: {round(av_deaths, 2)}")
            st.write(f"Average Assists: {round(av_assists, 2)}")
    with cols[1]:
        st.image(player_avatar)

    st.markdown(
        "<style>.line { border: 0.5px solid; margin: 0; }</style><div class='line'></div>",
        unsafe_allow_html=True)

    st.altair_chart(create_hero_bar_chart(data))
