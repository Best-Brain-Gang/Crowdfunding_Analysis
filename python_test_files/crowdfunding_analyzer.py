# Import the required libraries and dependencies
import os
import pandas as pd
import questionary
from pathlib import Path
from dotenv import load_dotenv
import sqlalchemy
import data_cleaner

# Add viz libs
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import hvplot.pandas
import altair as alt 
from bokeh.plotting import figure, show
import folium

# Force clean vars
force_clean_large_kickstarter = False
force_clean_small_kickstarter = False
force_clean_indiegogo = False

# Clean large kickstarter
my_kickstarter_large_file = Path('./Resources/kickstarter_data_clean/ks-projects-large.csv')
if not my_kickstarter_large_file.is_file() or force_clean_large_kickstarter:
    data_cleaner.clean_large_kickstarter()

# Import small kickstarter most backed dataset
kickstarter_large_clean_df = pd.read_csv(
    Path('./Resources/kickstarter_data_clean/ks-projects-large.csv')
)

# Fix dates
kickstarter_large_clean_df['launched'] = pd.to_datetime(kickstarter_large_clean_df['launched'])
kickstarter_large_clean_df['deadline'] = pd.to_datetime(kickstarter_large_clean_df['deadline'])

# View head
kickstarter_large_clean_df.head(2)

print(kickstarter_large_clean_df.head(2))


# # Clean small kickstarter
# my_kickstarter_small_file = Path('./Resources/kickstarter_data_clean/ks-projects-small.csv')
# if not my_kickstarter_small_file.is_file() or force_clean_small_kickstarter:
#     %run ./clean_kickstarter_small.ipynb

# # Clean indiegogo kickstarter
# my_indiegogo_file = Path('./Resources/indiegogo_data_clean/indiegogo-projects.csv')
# if not my_indiegogo_file.is_file() or force_clean_indiegogo:
#     %run ./clean_indiegogo.ipynb