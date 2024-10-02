import unittest
import pandas as pd
from food_search_all_functions import search_food

class TestFoodSearchFunctions(unittest.TestCase):

    def setUp(self):
        # Sample data to be used in tests
        self.df = pd.DataFrame({
            'food': ['apple', 'banana', 'carrot', 'apple pie'],
            'calories': [52, 89, 41, 300],
            'protein': [0.3, 1.1, 0.9, 2.5]
        })

    def test_search_food_valid_exact(self):
        # Test with a valid exact query
        result = search_food(self.df, 'apple')
        self.assertEqual(len(result), 2)  # Expecting 2 matches ('apple' and 'apple pie')

    def test_search_food_valid_partial(self):
        # Test with a valid partial query
        result = search_food(self.df, 'ban')
        self.assertEqual(len(result), 1)  # Expecting 1 match ('banana')
        self.assertIn('banana', result['food'].values)

    def test_search_food_case_insensitive(self):
        # Test with different cases (case-insensitive)
        result = search_food(self.df, 'CARROT')
        self.assertEqual(len(result), 1)  # Expecting 1 match ('carrot')
        self.assertIn('carrot', result['food'].values)

    def test_search_food_not_found(self):
        # Test with a query that does not exist
        result = search_food(self.df, 'mango')
        self.assertEqual(result, "Food item not found.")  # Expecting the 'not found' message

    def test_search_food_empty_query(self):
        # Test with an empty query
        result = search_food(self.df, '')
        self.assertEqual(len(result), 4)  # Expecting all rows since the query is empty

    def test_search_food_nan_values(self):
        # Test with NaN values in the 'food' column
        df_with_nan = self.df.copy()
        df_with_nan.loc[1, 'food'] = None
        result = search_food(df_with_nan, 'banana')
        self.assertEqual(len(result), 0)  # Expecting 0 matches since 'banana' is NaN

if __name__ == '__main__':
    unittest.main()
