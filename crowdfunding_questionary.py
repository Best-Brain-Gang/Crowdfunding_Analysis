# A Database CLI Application

# Import modules
import pandas as pd
import sqlalchemy as sql
import fire
import sys
import questionary

# Helps client select platform and provides statistics
def crowdfunder_platform_selector(available_categories, engine):
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
    print("Provide us with your project category and we will tell you which platform to use\n")
    print("based off of failed/success and funding statistics\n")

    # Use questionary, to ask for project category.
    category_type = questionary.text("Enter your project category:").ask()
    
    print("Running report ...")

    platform_to_use = 'Kickstarter'

    print(f"Based on your category of {category_type} you should use {platform_to_use} as your platform.")

    continue_running = questionary.confirm("Do you want to look at a different category?").ask()

    return continue_running


if __name__ == "__main__":

    # Database connection string to the avaialbe categories
    # TODO

    # Create an engine to interact with the database
    # TODO

    # Read the categories table into a dataframe called `available_categories`
    # TODO

    # Get a list of available categories
    # TODO

    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `crowdfunder_platform_selector` function.
    # Pass the `available_categories` DataFrame `sectors` and the database `engine` as parameters.
    while running:
        continue_running = crowdfunder_platform_selector(available_categories=['a', 'b', 'c'], engine='my_engine')
        if continue_running == 'y':
            running = True
        else:
            running = False

    print('Thanks for using...')