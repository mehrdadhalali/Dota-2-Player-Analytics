"""The dashboard"""

from os import environ as ENV

import streamlit as st
from dotenv import load_dotenv

from charts import create_hero_bar_chart, turn_into_dataframe, calculate_win_rate
from database import get_all_data

load_dotenv()

st.set_page_config(layout="wide")

if __name__ == "__main__":

    db_data = get_all_data()

    data = turn_into_dataframe(db_data)

    cols = st.columns([2, 0.5])
    with cols[0]:
        st.header(
            f"Welcome to your Dota 2 Analytics Dashboard, {ENV['PLAYER_NAME']}.")
        sub_cols = st.columns([1, 1, 1])
        with sub_cols[0]:
            wr_text = f"Win Rate: {calculate_win_rate(data)}%"
            st.markdown(f"<h3 style='text-align: center'> {wr_text} </h3>",
                        unsafe_allow_html=True)
    with cols[1]:
        st.image(ENV["PLAYER_AVATAR"])

    st.markdown(
        "<style>.line { border: 0.5px solid; margin: 0; }</style><div class='line'></div>",
        unsafe_allow_html=True)

    st.altair_chart(create_hero_bar_chart(data))
