"""
# My first app
Snowflake tutorial :)
"""

import numpy as np
import pandas as pd
import streamlit as st


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

