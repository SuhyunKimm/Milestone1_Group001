import pandas as pd
import re

def load_data(csv_file):
    """Loads the CSV file and converts numeric columns."""
    df = pd.read_csv(csv_file)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    return df

def search_food(df, search_text):
    """Search for food in the dataframe."""
    matches = df[df['food'].apply(lambda x: bool(re.search(search_text, str(x), re.IGNORECASE)))]
    return matches

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

def plot_nutrients(major_nutrients, food_name, ax1, ax2):
    """Plot pie chart and bar graph for nutrients."""
    names = list(major_nutrients.keys())
    values = list(major_nutrients.values())

    # Pie chart
    ax1.pie(values, labels=names, autopct='%1.1f%%', startangle=90, shadow=True)
    ax1.set_title(f"Pie Chart for {food_name}'s nutrition values")

    # Bar graph
    ax2.bar(names, values, color='skyblue')
    ax2.set_xlabel('Nutrients')
    ax2.set_ylabel('Values')
    ax2.set_title(f"Bar Graph for {food_name}'s nutrition values")
    ax2.set_xticks(range(len(names)))
    ax2.set_xticklabels(names, rotation=90)

def clear_previous_data(canvas, *texts):
    """Clear previous chart and texts."""
    if canvas is not None:
        canvas.Destroy()
    for text in texts:
        text.Hide()
