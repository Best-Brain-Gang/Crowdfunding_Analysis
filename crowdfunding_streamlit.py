import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import sqlalchemy
import hvplot.pandas
import altair as alt
import plotly.express as px
import pydeck as pdk
import pandas as pd
import math

######## Config ########
# Setup vars that can only be called one time
def setup_streamlit():
    # Setup page wide to make use of full screen
    st.set_page_config(layout="wide")

# Connect to the db
def connect_db():
    # Establishes Database Connection with a temporary SQL db (we can update to give it a name later)
    database_connection_string = "sqlite:///crowdfunding.db"

    engine = sqlalchemy.create_engine(database_connection_string)
    return engine

######## Main for navbar ########
def main():

    # Menu
    menu = ['Intro',
    'Members and Roles',
    'Duration Analysis',
    'Indiegogo',
    'USA Analysis']

    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Intro':
        setup_intro_page()
    elif choice == 'Members and Roles':
        setup_member_and_role_page()
    elif choice == 'Duration Analysis':
        setup_duration_page()
    elif choice == 'Indiegogo':
        setup_simple_page()
    else:
        setup_simple_page()

######## Pages setup ########
# Home page setup   
def setup_intro_page():
    # Add title
    st.title('Welcome to Crowdfunder Analyzer')

    # Add image at top
    kickstarter_vs_indiegogo = Image.open('./Resources/Images/kickstarter_indiegogo.jpeg')
    st.image(kickstarter_vs_indiegogo)

    # Add discription
    st.markdown(''' 
    # Crowdfunding Analysis
    This project attempts to help project creators understand how to market their project on Kickstarter vs Indiegogo or other crowdfunding platforms.
    The purpose of this tool is to not only give them some advice on platforms but be able to efficiently market their project.

    We did the following for this project:
    - We analyzed Kickstarter vs. Indiegogo using Jupyter notebook
    - We made an interactive command line "app" using questionary
    ''')

# Home page setup   
def setup_member_and_role_page():
    # Setup cols
    col1, col2 = st.beta_columns(2)

    # Add image at top
    image_i = Image.open('./Resources/Images/i_wordcloud.png')
    image_k = Image.open('./Resources/Images/k_wordcloud.png')
    col1.image(image_k)
    col2.image(image_i)

    # Add title
    st.title('Project Members and Roles')

    # Add slide
    team_members = Image.open('./Resources/Images/team_member.png')
    st.image(team_members)

# Simple example page layout
def setup_simple_page():
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

    # Use the full page instead of a narrow central column
    col1, col2 = st.beta_columns(2)

    # col1.write(line_chart)
    col1.line_chart(
        chart_data,
        height=500)
    col2.map(map_data)

# Setup duration page
def setup_duration_page():
    # Setup cols
    col1, col2 = st.beta_columns(2)

    st.title('Analysis of Duration')

    st.markdown(''' 
    # Crowdfunding Analysis
    This project attempts to help project creators understand how to market their project on Kickstarter vs Indiegogo or other crowdfunding platforms.
    The purpose of this tool is to not only give them some advice on platforms but be able to efficiently market their project.

    We did the following for this project:
    - We analyzed Kickstarter vs. Indiegogo using Jupyter notebook
    - We made an interactive command line "app" using questionary
    ''')

    # Setup cols
    col1, col2 = st.beta_columns(2)

    # Create a SQL query to get the main_category and duration of the Kickstarter Large dataframe.
    query_ks = """
    SELECT main_category, duration
    FROM kickstarter_large
    """
    query_indiegogo = """
    SELECT main_category, duration
    FROM indie_gogo
    """

    # This will let us read the query we applied earlier to create a dataframe.
    ks_large_duration_dataframe = pd.read_sql_query(
        query_ks, 
        con= engine)

    col1.subheader('Categories with Duration for Kickstarter')
    col1.dataframe(ks_large_duration_dataframe)

    indiegogo_duration_dataframe = pd.read_sql_query(
        query_indiegogo, 
        con= engine)
    
    col2.subheader('Categories with Duration for Indiegogo')
    col2.dataframe(indiegogo_duration_dataframe)

    # Create a SQL query to get the main_category and 
    # duration of the Kickstarter Large dataframe and 
    # group them by main_category and get its average duration days.
    query="""SELECT
    main_category, AVG(duration) AS average_duration_days
    FROM
    kickstarter_large
    GROUP BY
    main_category
    ORDER BY 
        AVG(duration) DESC,
        main_category DESC;
    """
    # This will let us read the query we applied earlier to create a dataframe.
    ks_large_groupby_maincategory_df = pd.read_sql_query(
        query, 
        con= engine)

    col1.subheader('Categories with Avg. Duration for Kickstarter')
    col1.dataframe(ks_large_groupby_maincategory_df)

    chart = alt.Chart(ks_large_groupby_maincategory_df).mark_bar().encode(
        alt.X('main_category',
            sort="-y"
        ),
        alt.Y('average_duration_days',
            scale=alt.Scale(zero=False)
        )
    )

    col2.subheader('Categories with Avg. Duration for Kickstarter')
    col2.altair_chart(chart)

    # Create a SQL query to get the total number of projects in Kickstarter Large dataframe per country.
    query_ks_country = """
    SELECT full_country_names AS Country, COUNT (*) AS Total_number_of_projects, lat, lon
    FROM kickstarter_large
    GROUP BY full_country_names
    ORDER BY
        total_number_of_projects DESC;
    """

    # This will let us read the query we applied earlier to create a dataframe.
    ks_country_total_df = pd.read_sql_query(
        query_ks_country, 
        con= engine)

    # This will create a scatter mapbox plot for Kickstarter and  their respective longitude and latitude plotted in with total number of projects.
    # Define a layer to display on a map
    layer = pdk.Layer(
        "ScatterplotLayer",
        ks_country_total_df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=10,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position='[lon, lat]',
        get_radius="Total_number_of_projects",
        get_fill_color=[124, 252, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
    view_state = pdk.ViewState(latitude=37.983810, longitude=-23.727539, zoom=1, bearing=0, pitch=0)


    st.subheader('Kickstarter number of projects by country map')
    
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{Country}\n{Total_number_of_projects}"}
        ))

######## Components ########

######## Main ########  
if __name__ == '__main__':
    setup_streamlit()
    engine = connect_db()
    main()

