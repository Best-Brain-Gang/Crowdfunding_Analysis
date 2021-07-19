import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")
# Use the full page instead of a narrow central column
col1, col2 = st.beta_columns(2)

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

line_chart = st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

my_map = st.map(map_data)

# col1.write(line_chart)
col1.line_chart(
    chart_data,
    height=500)
col2.map(map_data)
