"""
# My first app
Snowflake tutorial :)
"""

import numpy as np
import pandas as pd
import requests
import snowflake.connector
import streamlit as st
from urllib.error import URLError


st.title('Healthy Dining')

st.header('Breakfast Favourites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)

# Add picker to select a fruit
fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_list.index), default=['Apple', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the dataframe
st.dataframe(fruits_to_show)

st.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = st.text_input('What fruit do you want to know about?')
    if not fruit_choice:
        st.error('Please select a fruit to get information about!')
    else:
        fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        st.dataframe(fruityvice_normalized)
except URLError as e:
    st.error(e)

st.write('You selected:', fruit_choice)

# st.text(fruityvice_response.json())


st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_row)

# Allow the user to select a fruit from the list
add_my_fruit = st.text_input('What fruit do you want to add to the list?', 'jackfruit')
my_cur.execute(f"INSERT INTO fruit_load_list VALUES ('{add_my_fruit}')")
st.text(f"Thanks for adding {add_my_fruit} to the list!")
