# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/SuhyunKimm/Milestone1_Group001

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions** | **Test Functions**                               |
|----------------------|--------------------------------------------------|
| `get_data(path)`     | `test_get_data_valid()` <br> `test_get_data_invalid()`     |
| `search_food_by_name(df, name)`| `test_search_food_by_name_valid()` <br> `test_search_food_by_name_no_match()` <br>  `test_search_food_by_name_case_insensitivity` <br> `test_get_food_name_and_calorie_valid`|
| `get_food_name_and_calorie(df)`  | `test_get_food_name_and_calorie_empty()`                                            |

---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_get_data_valid()`
  - `test_get_data_invalid()`
- **Tested Function/Module**
  - `get_data(path)`
- **Description**
  - The testing functions are designed to verify that the `get_data` function successfully loads CSV data from a specified path and ensures that the file adheres to the expected format.

- **1) Valid Input and Expected Output**  

| **Valid Input**          | **Expected Output** |
|--------------------------|---------------------|
| `get_data('Food_Nutrition_Dataset.csv')`             | DataFrame type data |


- **1) Code for the Test Function**
```python
def test_get_data_valid() :
    filepath = 'Food_Nutrition_Dataset.csv'
    file = get_data(filepath)
    assert isinstance(file, pd.DataFrame)
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**              | **Expected Output** |
|--------------------------------|---------------------|
| `get_data('invalid_path.csv')` | `FileNotFoundError` |

- **2) Code for the Test Function**
```python
def test_get_data_invalid():
    filepath = 'invalid_path.csv'  # An intentionally invalid path
    with pytest.raises(FileNotFoundError):
        get_data(filepath)
```
### Test Case 2:
- **Test Function/Module**
  - `test_search_food_by_name_valid()`
  - `test_search_food_by_name_no_match()`
  - `test_search_food_by_name_case_insensitivity()`
- **Tested Function/Module**
  - `search_food_by_name(df, name)`
- **Description**
  - The testing functions are designed to confirm that the `search_food_by_name` function accurately retrieves data with matching names in a case-insensitive manner.
- **1) Valid Input and Expected Output**  

| **Valid Input**                              | **Expected Output**                                                            |
|----------------------------------------------|--------------------------------------------------------------------------------|
| `search_food_by_name(sample_data, 'melone')` | `pd.DataFrame({'food' : ['Watermelon', 'melon'], 'Caloric Value' : [62, 82]})` |
| `search_food_by_name(sample_data, 'apple')`  | `pd.DataFrame({'food' : ['Apple', 'Pineapple'],'Caloric Value' : [95, 105]})`  |

- **1) Code for the Test Function**
```python
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
```
- **2) Invalid Input and Expected Output (Not Matching)**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|--------------------|
| `search_food_by_name(sample_data, 'Mango')`| empty  |

- **2) Code for the Test Function**
```python
def test_search_food_by_name_no_match():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result = search_food_by_name(sample_data, 'Mango')
    assert result.empty
```
- **3) Valid Input and Expected Output (Case Insensitivity)**

| **Invalid Input**                             | **Expected Output** |
|-----------------------------------------------|--------------------|
| `search_food_by_name(sample_data, 'oRaNgEs')` | `pd.DataFrame({'food': ['Oranges'],'Caloric Value': [62]})`  |
| `search_food_by_name(sample_data, 'MeLoN')`   | `pd.DataFrame({'food': ['Watermelon', 'melon'],'Caloric Value': [62,82]})`  |

- **2) Code for the Test Function**
```python
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
```
### Test Case 3:
- **Test Function/Module**
  - `test_get_food_name_and_calorie_valid()`
  - `test_get_food_name_and_calorie_empty()`
- **Tested Function/Module**
  - `get_food_name_and_calorie(df)`
- **Description**
  - The testing functions are designed to ensure that the `get_food_name_and_calorie` function successfully generates a list of strings, each containing a food name along with its caloric value.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `get_food_name_and_calorie(sample_data)` | `['Apple (95 kcal)', 'Pineapple (105 kcal)', 'Watermelon (62 kcal)', 'melon (82 kcal)', 'Oranges (62 kcal)']`                 |

- **1) Code for the Test Function**
```python
def test_get_food_name_and_calorie_valid():
    sample_data = pd.DataFrame({
        'food': ['Apple', 'Pineapple', 'Watermelon', 'melon', 'Oranges'],
        'Caloric Value': [95, 105, 62, 82, 62]
    })
    result = get_food_name_and_calorie(sample_data)
    expected = ['Apple (95 kcal)', 'Pineapple (105 kcal)', 'Watermelon (62 kcal)', 'melon (82 kcal)', 'Oranges (62 kcal)']

    assert result == expected
```
- **2) Invalid Input and Expected Output (Empty dataframe)**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `get_food_name_and_calorie(empty_df)` | empty list `[]`      |

- **2) Code for the Test Function**
```python
def test_get_food_name_and_calorie_empty():
    empty_df = pd.DataFrame(columns = ['food', 'Caloric Value'])
    result = get_food_name_and_calorie(empty_df)
    expected = []

    assert result == expected
```

### Test Case 4:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```


### Test Case 5:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:

add more test cases if necessary.

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
