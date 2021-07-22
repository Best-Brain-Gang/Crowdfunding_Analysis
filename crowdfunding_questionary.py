# A Database CLI Application

# Import modules
import pandas as pd
import sqlalchemy as sql
import fire
import sys
import questionary
from IPython.display import display

# Function to load table into DB
# data is the dataframe we want to save, 
# table name is the name of the new table (as a string value), 
# and engine is the engine input established earlier
def new_table(data, table_name):
    data.to_sql(f"{table_name}", engine, index=True, if_exists="replace")


# Lets us load the table of our choice from the database, just set the function equal to a new dataframe variable and run 
# must set the table name as a string value
def load_full_table(table_name):
    new_df = pd.read_sql_table(f"{table_name}", con=engine )
    return new_df

# Helps client select platform and provides statistics
def crowdfunder_platform_selector(available_categories, ks_ig_df, engine):
    """Determine which platform to start project on

    Platform selection criteria is based on:
        - Project category

    Args:
        available_categories:
        engine:

    Returns:
        The platform the client should use along with statistics
    """

    # Print a welcome message for the application
    print("\n......Welcome to the Crowdfunding Platform Selector.....\n")
    print("Provide us with your project category and we will tell you which platform to use")
    print("based off of failed/success and funding statistics.\n")

    # Use questionary, to ask for project category.
    category_type = questionary.select(
        "What is your project category?\n",
        choices=available_categories,
        ).ask()
    
    print("\nRunning report ...\n")
    #TODO
    percent_stats = ks_ig_df.loc[category_type]
    high_success = percent_stats['percent_success_ks']
    low_success = percent_stats['percent_success_ig']

    platform_to_use = 'Kickstarter' if percent_stats['percent_success_ks'] > percent_stats['percent_success_ig'] else 'Indigogo'
    platform_not_to_use = 'Kickstarter' if percent_stats['percent_success_ks'] < percent_stats['percent_success_ig'] else 'Indigogo'

    if platform_to_use == 'Indiegogo':
        high_success = percent_stats['percent_success_ks']
        low_success = percent_stats['percent_success_ig']

    print(f"Based on your category of {category_type} you should use {platform_to_use} as your platform, because it has a success rate of {high_success:.2f} for this category. {platform_not_to_use} has a lower success rate of {low_success:.2f}.\n\n")

    continue_running = questionary.confirm("Do you want to look at a different category?\n").ask()

    return continue_running


if __name__ == "__main__":

    # Establishes Database Connection with a temporary SQL db (we can update to give it a name later)
    database_connection_string = "sqlite:///crowdfunding_db"
    engine = sql.create_engine(database_connection_string)

    # Get available categoriess
    percent_success_fail_ks_ig = load_full_table('percent_success_fail_ks_ig')
    percent_success_fail_ks_ig.set_index('main_category', inplace=True)
    avl_categories = list(percent_success_fail_ks_ig.index)

    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `crowdfunder_platform_selector` function.
    # Pass the `available_categories` DsataFrame `sectors` and the database `engine` as parameters.
    while running:  
        running = crowdfunder_platform_selector(available_categories=avl_categories, ks_ig_df=percent_success_fail_ks_ig, engine=engine)

    print('\nThanks for using...\n')