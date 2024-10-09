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

def test_extract_nutrient_info():
    sample_data = pd.Series({
        'food': 'Apple',
        'Caloric Value': 52,
        'Fat': 0.2,
        'Sugar': 10.0,
        'Protein': 0.3
    })
    nutrient_info = extract_nutrient_info(sample_data)
    expected_nutrients = {
        'Fat': 0.2,
        'Sugar': 10.0,
        'Protein': 0.3
    }
    assert nutrient_info == expected_nutrients

def test_prepare_nutrients():
    nutrients = {'Protein': 1.5, 'Carbs': 0.5, 'Fat': 0.0, 'Sugars': 0.8}
    major_nutrients = prepare_nutrients(nutrients)
    assert 'Protein' in major_nutrients
    assert 'Carbs' not in major_nutrients
    assert 'Sugars' not in major_nutrients
    assert 'Other Nutrients' in major_nutrients


def test_filter_foods_by_nutrient_valid_range():
    df = get_data('Food_Nutrition_Dataset.csv')
    sample_data = pd.DataFrame({
        'food': ['camembert cheese', 'goat cheese', 'brie cheese', 'goat cheese soft', 'honey'],
        'Caloric Value': [90, 103, 100, 75, 64]
    })
    food_list, message = filter_foods_by_nutrient(df, 'Caloric Value', 60, 70)

    assert 'honey' in food_list
    assert "Foods in range for Caloric Value" in message


def test_filter_foods_by_nutrient_no_foods_in_range():
    df = get_data('Food_Nutrition_Dataset.csv')
    sample_data = pd.DataFrame({
        'food': ['camembert cheese', 'goat cheese', 'brie cheese', 'goat cheese soft', 'honey'],
        'Caloric Value': [90, 103, 100, 75, 64]
    })
    food_list, message = filter_foods_by_nutrient(df, 'Caloric Value', 4000, 5000)

    assert food_list == []
    assert "No foods found for Caloric Value" in message


def test_filter_foods_by_nutrient_invalid_nutrient():
    df = get_data('Food_Nutrition_Dataset.csv')
    sample_data = pd.DataFrame({
        'food': ['camembert cheese', 'goat cheese', 'brie cheese', 'goat cheese soft', 'honey'],
        'Caloric Value': [90, 103, 100, 75, 64]
    })
    food_list, message = filter_foods_by_nutrient(df, '', 50, 100)
    assert food_list == []
    assert "Nutrient '' not found" in message

def test_categorize_nutrition_low():
    assert categorize_nutrition(5, 30) == 'low'

def test_categorize_nutrition_mid():
    assert categorize_nutrition(15, 30) == 'mid'

def test_categorize_nutrition_high():
    assert categorize_nutrition(25, 30) == 'high'

def test_categorize_nutrition_missing_value():
    assert categorize_nutrition(float('nan'), 30) == 'unknown'

def test_categorize_nutrition_zero_max_value():
    assert categorize_nutrition(0, 0) == 'high'  # Edge case handling


def test_nutrition_level_filter_basic():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [40, 90, 150],
        "sugar": [8, 15, 30]
    })
    result = nutrition_level_filter(df)

    expected = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": ["low", "mid", "high"],
        "sugar": ["low", "mid", "high"]
    })
    pd.testing.assert_frame_equal(result, expected)


def test_nutrition_level_filter_with_zero_values():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [0, 50, 100],
        "sugar": [0, 0, 30]
    })
    result = nutrition_level_filter(df)

    expected = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": ["low", "mid", "high"],
        "sugar": ["low", "low", "high"]
    })
    pd.testing.assert_frame_equal(result, expected)


def test_nutrition_level_filter_non_numeric_columns():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [40, 90, 150],
        "description": ["tasty", "yellow", "crunchy"]
    })
    result = nutrition_level_filter(df)

    expected = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": ["low", "mid", "high"],
        "description": ["tasty", "yellow", "crunchy"]
    })
    pd.testing.assert_frame_equal(result, expected)


def test_nutrition_level_filter_all_zero_values():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [0, 0, 0],
        "sugar": [0, 0, 0]
    })
    result = nutrition_level_filter(df)

    expected = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": ["high", "high", "high"],
        "sugar": ["high", "high", "high"]
    })
    pd.testing.assert_frame_equal(result, expected)


def test_nutrition_level_filter_empty_dataframe():
    df = pd.DataFrame(columns=["food", "calories", "sugar"])
    result = nutrition_level_filter(df)

    expected = pd.DataFrame(columns=["food", "calories", "sugar"])
    pd.testing.assert_frame_equal(result, expected)


def test_nutrition_level_filter_mixed_data_types():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [40, 90, 150],
        "sugar": ["10", "20", "30"]  # sugar values are strings
    })
    result = nutrition_level_filter(df)

    expected = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": ["low", "mid", "high"],
        "sugar": ["10", "20", "30"]
    })
    pd.testing.assert_frame_equal(result, expected)
def test_filter_by_nutrition_and_level_valid():
    # Sample data for testing
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon'],
        'Caloric Value': [20, 50, 90],
        'Protein': [2, 5, 8]
    })

    result = filter_by_nutrition_and_level(sample_data, 'Caloric Value', 'mid')

    expected = pd.DataFrame({
        'food': ['Pineapple'],
        'Caloric Value': [50]
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))




def test_filter_by_nutrition_and_level_invalid_nutrition_type():

    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [50, 100, 150],
        "sugar": [10, 20, 30]
    })
    result = filter_by_nutrition_and_level(df, "fiber", "low")

    assert result == "Invalid nutrition type."


def test_filter_by_nutrition_and_level_no_matching_level():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [50, 100, 150],
        "sugar": [10, 20, 30]
    })
    result = filter_by_nutrition_and_level(df, "calories", "very high")

    assert result == "No foods found with calories at very high level."


def test_filter_by_nutrition_and_level_empty_dataframe():
    df = pd.DataFrame(columns=["food", "calories", "sugar"])
    result = filter_by_nutrition_and_level(df, "calories", "low")

    assert result == "No foods found with calories at low level."


def test_filter_by_nutrition_and_level_multiple_matching_rows():
    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot", "grapes"],
        "calories": [40, 80, 150, 70],
        "sugar": [10, 20, 30, 15]
    })
    result = filter_by_nutrition_and_level(df, "calories", "mid")


    expected = pd.DataFrame({
        "food": ["banana", "grapes"],
        "calories": [80, 70]
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))


def test_filter_by_nutrition_and_level_non_categorical_nutrition():

    df = pd.DataFrame({
        "food": ["apple", "banana", "carrot"],
        "calories": [40, 90, 150],
        "sugar": [8, 20, 30]
    })
    result = filter_by_nutrition_and_level(df, "sugar", "low")


    expected = pd.DataFrame({
        "food": ["apple"],
        "sugar": [8]
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
