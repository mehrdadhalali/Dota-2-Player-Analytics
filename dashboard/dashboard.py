"""The dashboard"""

import streamlit as st

from charts import create_hero_bar_chart, turn_into_dataframe
from database import get_all_data

if __name__ == "__main__":

    db_data = get_all_data()

    data = turn_into_dataframe(db_data)

    st.altair_chart(create_hero_bar_chart(data))
