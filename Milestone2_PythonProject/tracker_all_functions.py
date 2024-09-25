import pandas as pd

def get_data(path) :
    df = pd.read_csv(path)
    df = pd.read_csv('Food_Nutrition_Dataset.csv')
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


# print(df.columns)
# print(get_food_name_and_calorie(df))
