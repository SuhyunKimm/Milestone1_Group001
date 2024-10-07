import wx
from food_search_all_functions import *
from template_food_search_panel import FoodSearchPanel


class PanelFoodSearch(FoodSearchPanel):
    def __init__(self, parent):
        super().__init__(parent)

        # Initialize variables for search and data management
        self.df = pd.read_csv('Food_Nutrition_Dataset.csv')
        self.search_results = None
        self.selected_item = None

    def food_search_go_back_btn_click(self, event):
        """Handles the Go Back button click."""
        print("Go Back button clicked!")
        self.GetParent().go_to_main()

    def food_search_search_btn_click(self, event):
        """Handles the Search button click."""
        search_query = self.m_textCtrl5.GetValue().strip().lower()
        if not search_query:
            wx.MessageBox("Please enter a search term.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

        # Perform the search and store results
        self.search_results = search_food(self.df, search_query)

        # Update the grid with the search results
        self.populate_search_results(self.search_results)

    def populate_search_results(self, results_df):
        """Updates the grid with search results from the DataFrame."""
        if results_df is None or results_df.empty:
            wx.MessageBox("No results found.", "Info", wx.OK | wx.ICON_INFORMATION)
            self.m_grid7.ClearGrid()
            return

        # Ensure results_df is a DataFrame
        if isinstance(results_df, pd.Series):
            results_df = results_df.to_frame().T

        rows, cols = results_df.shape

        # Get the current number of rows and columns
        current_rows = self.m_grid7.GetNumberRows()
        current_cols = self.m_grid7.GetNumberCols()

        # Adjust the number of rows
        if current_rows < rows:
            self.m_grid7.AppendRows(rows - current_rows)
        elif current_rows > rows:
            self.m_grid7.DeleteRows(0, current_rows - rows)

        # Adjust the number of columns
        if current_cols < cols:
            self.m_grid7.AppendCols(cols - current_cols)
        elif current_cols > cols:
            self.m_grid7.DeleteCols(0, current_cols - cols)

        # Set column labels
        for col_idx, col_label in enumerate(results_df.columns):
            self.m_grid7.SetColLabelValue(col_idx, col_label)

        # Populate the grid with data
        for row_idx in range(rows):
            for col_idx in range(cols):
                self.m_grid7.SetCellValue(row_idx, col_idx, str(results_df.iat[row_idx, col_idx]))

    def update_grid(self, result_series):
        """Updates the grid with a single search result (series)."""
        self.m_grid7.ClearGrid()

        # Set the number of columns and rows based on the data
        columns = result_series.index.tolist()
        values = result_series.values.tolist()

        # Create grid for 1 row and the number of columns in the result
        self.m_grid7.CreateGrid(1, len(columns))

        # Set the column labels
        for idx, col in enumerate(columns):
            self.m_grid7.SetColLabelValue(idx, col)

        # Set the values in the grid
        for idx, value in enumerate(values):
            self.m_grid7.SetCellValue(0, idx, str(value))

