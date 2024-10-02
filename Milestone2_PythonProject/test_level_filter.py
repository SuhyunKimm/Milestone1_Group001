import unittest
import pandas as pd
from unittest.mock import patch

from level_filter_all_functions import categorize_nutrition, nutrition_level_filter, filter_by_nutrition_and_level


class TestNutritionFunctions(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
