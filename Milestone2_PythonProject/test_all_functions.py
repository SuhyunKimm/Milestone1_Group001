import pytest

from all_functions import *

def test_get_data_valid() :
    filepath = 'Food_Nutrition_Dataset.csv'
    file = get_data(filepath)
    assert isinstance(file, pd.DataFrame)

def test_get_data_invalid():
    filepath = 'invalid_path.csv'  # An intentionally invalid path
    with pytest.raises(FileNotFoundError):
        get_data(filepath)

def test_search_food_by_name_valid():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result1 = search_food_by_name(sample_data, 'melon').reset_index(drop=True)
    expected1 = pd.DataFrame({
        'food': ['Watermelon', 'melon'],
        'Caloric Value': [62, 82]
    })

    assert isinstance(result1, pd.DataFrame)
    assert result1.equals(expected1)

    result2 = search_food_by_name(sample_data, 'apple').reset_index(drop=True)
    expected2 = pd.DataFrame({
        'food' : ['Apple', 'Pineapple'],
        'Caloric Value' : [95, 105]
    })

    assert isinstance(result2, pd.DataFrame)
    assert result2.equals(expected2)

def test_search_food_by_name_no_match():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result = search_food_by_name(sample_data, 'Mango')
    assert result.empty

def test_search_food_by_name_case_insensitivity():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result1 = search_food_by_name(sample_data, 'oRaNgEs').reset_index(drop=True)
    expected1 = pd.DataFrame({
        'food': ['Oranges'],
        'Caloric Value': [62]
    })

    assert isinstance(result1, pd.DataFrame)
    assert result1.equals(expected1)

    result2 = search_food_by_name(sample_data, 'MeLoN').reset_index(drop=True)
    expected2 = pd.DataFrame({
        'food': ['Watermelon', 'melon'],
        'Caloric Value': [62,82]
    })

    assert isinstance(result2, pd.DataFrame)
    assert result2.equals(expected2)

def test_get_food_name_and_calorie_valid():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result = get_food_name_and_calorie(sample_data)
    expected = ['Apple (95 kcal)', 'Pineapple (105 kcal)', 'Watermelon (62 kcal)', 'melon (82 kcal)', 'Oranges (62 kcal)']
    assert result == expected

def test_get_food_name_and_calorie_empty():
    empty_df = pd.DataFrame(columns = ['food', 'Caloric Value'])
    result = get_food_name_and_calorie(empty_df)
    expected = []

    assert result == expected

def test_prepare_nutrients():
    nutrients = {'Protein': 1.5, 'Carbs': 0.5, 'Fat': 0.0, 'Sugars': 0.8}
    major_nutrients = prepare_nutrients(nutrients)
    assert 'Protein' in major_nutrients
    assert 'Carbs' not in major_nutrients
    assert 'Sugars' not in major_nutrients
    assert 'Other Nutrients' in major_nutrients

def test_filter_foods_by_nutrient_valid_range():
    df = get_data('Food_Nutrition_Dataset.csv')
    food_list, message = filter_foods_by_nutrient(df, 'Caloric Value', 50, 100)
    
    assert 'cream cheese' in food_list                                                          #Expected food found in valid range
    assert "Foods in range for Caloric Value" in message

def test_filter_foods_by_nutrient_no_foods_in_range():
    df = get_data('Food_Nutrition_Dataset.csv')
    food_list, message = filter_foods_by_nutrient(df, 'Caloric Value', 4000, 5000)
    
    assert food_list == []                                                                      #Should not return any foods for invalid range
    assert "No foods found for Caloric Value" in message

def test_filter_foods_by_nutrient_invalid_nutrient():
    df = get_data('Food_Nutrition_Dataset.csv')
    food_list, message = filter_foods_by_nutrient(df, '', 50, 100)
    
    assert food_list == []                                                                     #Should not return any foods for unknown nutrient
    assert "Nutrient '' not found" in message
