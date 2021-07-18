# Import the required libraries and dependencies
import pandas as pd
from pathlib import Path

def clean_large_kickstarter():
    # Import large kickstarter recent dataset
    kickstarter_large_recent_df = pd.read_csv(
        Path('./Resources/kickstarter_data/ks-projects-201801.csv'),
    )

    # Imported data has a space at the end of the column name
    # Remove spaces in columns name
    kickstarter_large_recent_df.columns = kickstarter_large_recent_df.columns.str.replace(' ','')

    # Set the index as the ID
    kickstarter_large_recent_df.set_index('ID', inplace=True)

    # Kickstarter code to fix dates
    kickstarter_large_recent_df['launched'] = pd.to_datetime(kickstarter_large_recent_df['launched'])
    kickstarter_large_recent_df['deadline'] = pd.to_datetime(kickstarter_large_recent_df['deadline'])

    # Only pull out failed and successful cases to match indiegogo df
    failure_success = ['failed','successful']

    # Quick check to see if we have already renamed state col
    if 'failed' in kickstarter_large_recent_df['state'].values:
        kickstarter_large_recent_df = kickstarter_large_recent_df[kickstarter_large_recent_df['state'].isin(failure_success)]
        # Rename successful -> 1 and failed -> 0 to match indiegogo
        kickstarter_large_recent_df['state'].replace({'failed': '0', 'successful': '1'}, inplace=True)
        # Fix types
        kickstarter_large_recent_df = kickstarter_large_recent_df.astype({'state': 'int64'})

    # Sometimes projects are successful with no backers. Remove this data
    kickstarter_large_recent_df.drop(kickstarter_large_recent_df[(kickstarter_large_recent_df['state'] == 1) & (kickstarter_large_recent_df['backers'] == 0)].index, inplace = True)

    # Remove all countries with that have euro currency and country equal to N,0"
    kickstarter_large_recent_df.drop(kickstarter_large_recent_df[(kickstarter_large_recent_df['currency'] == 'EUR') & (kickstarter_large_recent_df['country'] == 'N,0"')].index, inplace = True)

    # Create a dictionary of country and currency pairs to fix other N,0" countries to right country
    country_currency_df = kickstarter_large_recent_df.loc[:,['country', 'currency']]
    country_currency_df.drop(kickstarter_large_recent_df[kickstarter_large_recent_df['country'] == 'N,0"'].index, inplace=True)
    country_currency_df.drop_duplicates(inplace=True)
    country_currency_df.set_index('currency', inplace = True)
    currency_country_dict = country_currency_df.to_dict()['country']

    # Function to clean up country col
    def replace_N0(country, currency):
        if country == 'N,0"':
            return currency_country_dict[currency]
        else:
            return country

    # Clean up all the N,0" values for countries using the currency_country_dict
    kickstarter_large_recent_df['country'] = kickstarter_large_recent_df.apply(lambda row: replace_N0(row['country'], row['currency']), axis=1)

    # List of columns to drop
    kickstarter_cols_drop = ['category', 'goal', 'pledged', 'usdpledged']

    # Selected columns kickstarter df
    kickstarter_selected_cols_large_recent_df = kickstarter_large_recent_df.drop(kickstarter_cols_drop, axis=1)

    # Duration
    kickstarter_selected_cols_large_recent_df['duration'] = kickstarter_selected_cols_large_recent_df['deadline'] - kickstarter_selected_cols_large_recent_df['launched'] 
    kickstarter_selected_cols_large_recent_df['duration'] = kickstarter_selected_cols_large_recent_df['duration'].dt.days

    # Daily Goal 
    kickstarter_selected_cols_large_recent_df['daily_goal'] = round(kickstarter_selected_cols_large_recent_df['usd_goal_real'] / kickstarter_selected_cols_large_recent_df['duration'],2)

    # Daily Pledged
    kickstarter_selected_cols_large_recent_df['daily_pledged'] = round(kickstarter_selected_cols_large_recent_df['usd_pledged_real'] / kickstarter_selected_cols_large_recent_df['duration'],2)

    # Funded Percentage
    kickstarter_selected_cols_large_recent_df['funded_percent'] = round(kickstarter_selected_cols_large_recent_df['usd_pledged_real'] / kickstarter_selected_cols_large_recent_df['usd_goal_real'],4)

    # Average Backer Per Day
    kickstarter_selected_cols_large_recent_df['avg_backer_per_day'] = round(kickstarter_selected_cols_large_recent_df['backers'] / kickstarter_selected_cols_large_recent_df['duration'],2)

    # Pledged Per Person
    kickstarter_selected_cols_large_recent_df['pledged_per_person'] = round(kickstarter_selected_cols_large_recent_df['usd_pledged_real'] / kickstarter_selected_cols_large_recent_df['backers'],2)
    kickstarter_selected_cols_large_recent_df['pledged_per_person'] = kickstarter_selected_cols_large_recent_df['pledged_per_person'].fillna(0)

    # Fix types
    kickstarter_selected_cols_large_recent_df = kickstarter_selected_cols_large_recent_df.astype({"funded_percent": 'float', "avg_backer_per_day":'float', "pledged_per_person": 'float'})

    # Base column names for reordering
    base_order = ['name', 'main_category', 'currency', 'usd_goal_real', 'usd_pledged_real', 'deadline', 'launched', 'state', 'funded_percent','duration', 'daily_goal', 'daily_pledged', 'country']
    kickstarter_order = base_order + ['avg_backer_per_day', 'pledged_per_person']

    # Reorder each df
    kickstarter_selected_cols_large_recent_df = kickstarter_selected_cols_large_recent_df[kickstarter_order]

    kickstarter_selected_cols_large_recent_df.to_csv('./Resources/kickstarter_data_clean/ks-projects-large.csv')