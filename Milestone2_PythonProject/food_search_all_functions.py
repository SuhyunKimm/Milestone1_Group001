import pandas as pd
df = pd.read_csv('./Food_Nutrition_Dataset.csv')


# Function to search for nutritional data based on food name input
def search_food(df,food_name):
    df.set_index('food', inplace=True)
    if food_name in df.index:
        result_df = df.loc[food_name].to_frame().T
        return result_df
    else:
        return "Food item not found."
