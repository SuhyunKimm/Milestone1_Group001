import pandas as pd

# Load the dataset
df = pd.read_csv('./Food_Nutrition_Dataset.csv')

# Function to search for nutritional data based on partial food name input
def search_food(df, food_name):
    """Searches for nutritional data of foods containing the specified food name."""
    # Search for foods that contain the food_name (case-insensitive)
    matching_rows = df[df['food'].str.contains(food_name, case=False, na=False)]

    # If matching rows are found, return them
    if not matching_rows.empty:
        return matching_rows
    else:
        return "Food item not found."

