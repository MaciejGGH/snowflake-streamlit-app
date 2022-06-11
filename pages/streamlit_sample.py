"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import pandas as pd
import streamlit as st
import time

'## Admonitions:'

'> :warning: **Warning:** Do not push the big red button.'

'> :memo: **Note:** Sunrises are beautiful.'

'> :bulb: **Tip:** Remember to appreciate the little things in life.'

st.warning('> :warning: **Warning:** Do not push the big red button.')

st.info('> :memo: **Note:** Sunrises are beautiful.')

st.error('> :bulb: **Tip:** Remember to appreciate the little things in life.')


temp_data = pd.read_csv("h:\projects\humidity_temp.csv", names=['datetime', 'humidity', 'temperature'])
temp_data['datetime'] = pd.to_datetime(temp_data['datetime'])
temp_data.set_index(temp_data['datetime'], inplace=True)

st.header('Temperature data table:')
st.dataframe(temp_data[['temperature', 'humidity']])

st.header('Temperature chart:')

st.line_chart(temp_data[['temperature', 'humidity']].tail(1500))

st.header('Dummy chart:')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('Dummy map:')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [5, 10] + [52.4, 21.0],
    columns=['lat', 'lon'])

st.map(map_data)

import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.header('JSON:')
st.json(df.to_json())

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

