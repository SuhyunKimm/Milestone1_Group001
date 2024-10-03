import pytest

from tracker_all_functions import *
from breakdown_all_functions import *
from food_search_all_functions import *
from range_filter_all_functions import *
from level_filter_all_functions import *

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

def setUp(self):
     # Sample dataset to use in tests
    self.df = pd.DataFrame({
        'food': ['apple', 'banana', 'carrot', 'donut'],
        'calories': [52, 89, 41, 452],
        'protein': [0.3, 1.1, 0.9, 4.0],
        'fat': [0.2, 0.3, 0.1, 25.0]
    })
def test_categorize_nutrition_low(self):
    # Test low value categorization
    result = categorize_nutrition(10, 100)
    self.assertEqual(result, 'low')

def test_categorize_nutrition_mid(self):
    # Test mid value categorization
    result = categorize_nutrition(50, 100)
    self.assertEqual(result, 'mid')

def test_categorize_nutrition_high(self):
    # Test high value categorization
    result = categorize_nutrition(80, 100)
    self.assertEqual(result, 'high')

def test_categorize_nutrition_unknown(self):
    # Test NaN value categorization
    result = categorize_nutrition(float('nan'), 100)
    self.assertEqual(result, 'unknown')

def test_nutrition_level_filter(self):
    # Test the nutrition level filter on the sample dataset
    df_filtered = nutrition_level_filter(self.df)
    expected_values = {
        'calories': ['low', 'low', 'low', 'high'],
        'protein': ['low', 'low', 'low', 'high'],
        'fat': ['low', 'low', 'low', 'high']
    }

    # Verify the filtered DataFrame
    for col in expected_values:
        self.assertListEqual(df_filtered[col].tolist(), expected_values[col])

@patch('nutrition_functions.df', new_callable=lambda: pd.DataFrame({
    'food': ['apple', 'banana', 'carrot', 'donut'],
    'calories': [52, 89, 41, 452],
    'protein': [0.3, 1.1, 0.9, 4.0],
    'fat': [0.2, 0.3, 0.1, 25.0]
}))
def test_filter_by_nutrition_and_level_valid(self, mock_df):
    # Test filtering by a valid nutrition type and level
    result = filter_by_nutrition_and_level('calories', 'low')
    expected_result = pd.DataFrame({
        'food': ['apple', 'banana', 'carrot'],
        'calories': ['low', 'low', 'low']
    })

    pd.testing.assert_frame_equal(result, expected_result)

@patch('nutrition_functions.df', new_callable=lambda: pd.DataFrame({
    'food': ['apple', 'banana', 'carrot', 'donut'],
    'calories': [52, 89, 41, 452],
    'protein': [0.3, 1.1, 0.9, 4.0],
    'fat': [0.2, 0.3, 0.1, 25.0]
}))
def test_filter_by_nutrition_and_level_invalid_type(self, mock_df):
    # Test filtering by an invalid nutrition type
    result = filter_by_nutrition_and_level('fiber', 'low')
    self.assertEqual(result, "Invalid nutrition type.")

@patch('nutrition_functions.df', new_callable=lambda: pd.DataFrame({
    'food': ['apple', 'banana', 'carrot', 'donut'],
    'calories': [52, 89, 41, 452],
    'protein': [0.3, 1.1, 0.9, 4.0],
    'fat': [0.2, 0.3, 0.1, 25.0]
}))
def test_filter_by_nutrition_and_level_no_results(self, mock_df):
    # Test filtering by a valid nutrition type but with no matching results
    result = filter_by_nutrition_and_level('calories', 'mid')
    self.assertEqual(result, "No foods found with calories at mid level.")

