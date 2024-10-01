import pandas as pd
df = pd.read_csv('./Food_Nutrition_Dataset.csv')

def categorize_nutrition(value, max_value):
    if value < 0.33 * max_value:
        return 'low'
    elif 0.33 * max_value <= value < 0.66 * max_value:
        return 'mid'
    else:
        return 'high'


# Function to apply nutrition level filter (low, mid, high) based on max values
def nutrition_level_filter(df):
    df_filtered = df.copy()  # Create a copy of the DataFrame to modify

    for column in df_filtered.columns:
        max_value = df_filtered[column].max()  # Get the max value in the column
        df_filtered[column] = df_filtered[column].apply(lambda x: categorize_nutrition(x, max_value))

    return df_filtered


# Function to filter based on user input (type of nutrition and desired level)
def filter_by_nutrition_and_level(nutrition_type, desired_level):
    # Ensure the user input is valid
    if nutrition_type not in df.columns:
        return "Invalid nutrition type."

    # Apply the nutrition level filter to categorize the values in the DataFrame
    df_filtered = nutrition_level_filter(df)

    # Filter the DataFrame by the chosen nutrition type and level
    filtered_df = df_filtered[df_filtered[nutrition_type] == desired_level]

    if filtered_df.empty:
        return f"No foods found with {nutrition_type} at {desired_level} level."
    else:
        return filtered_df
