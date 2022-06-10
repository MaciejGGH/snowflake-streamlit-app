import pandas
import streamlit


streamlit.title('Healthy Dining')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)

# Add picker to select a fruit
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), default=['Apple', 'Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the dataframe
streamlit.dataframe(fruits_to_show)
