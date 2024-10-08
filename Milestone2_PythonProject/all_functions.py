import pandas as pd

def get_data(path) :
    df = pd.read_csv(path)
    return df

def search_food_by_name(df, name) :
    new_df = df[df['food'].str.contains(name, case=False)]
    return new_df

def get_food_name_and_calorie(df) :
    name_list = list(df['food'])
    cal_list = list(df['Caloric Value'])
    output = []
    for i in range(len(name_list)):
        output.append(f'{name_list[i]} ({cal_list[i]} kcal)')
    return output


def extract_nutrient_info(result):
    """Extract nutrient information from the result."""
    nutrient_names = list(result.index[2:-1])
    nutrients = {name: result[name] for name in nutrient_names}
    return nutrients


def prepare_nutrients(nutrients):
    """Prepare major and other nutrients for plotting."""
    major_nutrients = {}
    other_nutrients_value = 0

    for name, value in nutrients.items():
        if pd.notna(value):
            if value >= 1:
                major_nutrients[name] = value
            else:
                other_nutrients_value += value

    if other_nutrients_value > 0:
        major_nutrients['Other Nutrients'] = other_nutrients_value

    return major_nutrients


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
def filter_by_nutrition_and_level(df,nutrition_type, desired_level):
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


def filter_foods_by_nutrient(df, RF_nutrient_name, RF_min_value, RF_max_value):
    """Filters the food data based on the nutrient range."""

    if RF_nutrient_name in df.columns:
        filtered_foods = df[(df[RF_nutrient_name] >= RF_min_value) & (df[RF_nutrient_name] <= RF_max_value)]
        if not filtered_foods.empty:
            return filtered_foods['food'].tolist(), f"Foods in range for {RF_nutrient_name}."
        else:
            return [], f"No foods found for {RF_nutrient_name} in the selected range."
    else:
        return [], f"Nutrient '{RF_nutrient_name}' not found."

