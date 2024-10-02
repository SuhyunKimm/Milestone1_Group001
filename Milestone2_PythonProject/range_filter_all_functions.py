import pandas as pd

def load_data(csv_file):
    """Loads the CSV file and converts numeric columns."""
    df = pd.read_csv(csv_file)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    return df

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
