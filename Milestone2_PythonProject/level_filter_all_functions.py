import pandas as pd

# Load the dataset
df = pd.read_csv('./Food_Nutrition_Dataset.csv')

# Assume the DataFrame has a "Food Name" column.
# Convert numeric columns to appropriate data types to avoid type issues
for column in df.columns:
    if column != "food":  # Exclude "Food Name" from numeric conversion
        df[column] = pd.to_numeric(df[column], errors='coerce')

def categorize_nutrition(value, max_value):
    """Categorizes the nutrition value as low, mid, or high based on the max value in the column."""
    if pd.isna(value):
        return 'unknown'  # Handle missing or non-numeric values
    if value < 0.33 * max_value:
        return 'low'
    elif 0.33 * max_value <= value < 0.66 * max_value:
        return 'mid'
    else:
        return 'high'

# Function to apply nutrition level filter (low, mid, high) based on max values
def nutrition_level_filter(df):
    """Applies nutrition level filtering to categorize each value in the DataFrame."""
    df_filtered = df.copy()  # Create a copy of the DataFrame to modify

    # Categorize values for each column
    for column in df_filtered.columns:
        if column != "food" and pd.api.types.is_numeric_dtype(df_filtered[column]):
            max_value = df_filtered[column].max()  # Get the max value in the column
            df_filtered[column] = df_filtered[column].apply(lambda x: categorize_nutrition(x, max_value))

    return df_filtered

# Function to filter based on user input (type of nutrition and desired level)
def filter_by_nutrition_and_level(nutrition_type, desired_level):
    """Filters the DataFrame by a given nutrition type and level (low, mid, high)."""
    # Ensure the user input is valid
    if nutrition_type not in df.columns:
        return "Invalid nutrition type."

    # Apply the nutrition level filter to categorize the values in the DataFrame
    df_filtered = nutrition_level_filter(df)

    # Filter the DataFrame by the chosen nutrition type and level, including the "Food Name"
    filtered_df = df[df_filtered[nutrition_type] == desired_level][["food", nutrition_type]]

    if filtered_df.empty:
        return f"No foods found with {nutrition_type} at {desired_level} level."
    else:
        return filtered_df
