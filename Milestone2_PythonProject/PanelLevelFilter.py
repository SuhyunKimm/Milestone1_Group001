import wx
from all_functions import *  # Import necessary functions
from template_level_filter_panel import LevelFilterPanel


class PanelLevelFilter(LevelFilterPanel):
    def __init__(self, parent):
        super().__init__(parent)

        # Load the dataset using the get_data function
        self.df = get_data('Food_Nutrition_Dataset.csv')

        # Populate choices for the dropdown menus using the column names from the dataset
        self.m_choice3.SetItems([col for col in self.df.columns if col != 'food'])  # Set items for nutrition type, excluding the 'food' column
        self.m_choice4.SetItems(["low", "mid", "high"])  # Set items for nutrition level

    def level_filter_go_back_btn_click(self, event):
        """Handles the Go Back button click."""
        print("Go Back button clicked!")
        self.GetParent().go_to_main()
        self.food_search_reset()

    def nutrition_type_choice(self, event):
        """Handles selection of Nutrition type."""
        selected_nutrition_type = self.m_choice3.GetStringSelection()
        print(f"Selected Nutrition Type: {selected_nutrition_type}")

    def nutrition_level_choice(self, event):
        """Handles selection of Nutrition level."""
        selected_nutrition_level = self.m_choice4.GetStringSelection()
        print(f"Selected Nutrition Level: {selected_nutrition_level}")

    def level_filter_search_btn_click(self, event):
        """Handles the Search button click."""
        # Get the selected values from the dropdown menus
        nutrition_type = self.m_choice3.GetStringSelection()
        nutrition_level = self.m_choice4.GetStringSelection()

        # Ensure both a nutrition type and level are selected
        if not nutrition_type or not nutrition_level:
            wx.MessageBox("Please select both nutrition type and nutrition level.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

        # Filter the DataFrame using the filter_by_nutrition_and_level function
        filtered_df = filter_by_nutrition_and_level(nutrition_type, nutrition_level)

        # Handle the case where no matches are found or display the filtered data
        if isinstance(filtered_df, str):  # When no results or error message is returned
            wx.MessageBox(filtered_df, "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            self.populate_grid(filtered_df)

    def populate_grid(self, data_frame):
        """Populates the wx.Grid with the data from the filtered DataFrame."""
        rows, cols = data_frame.shape

        # Clear existing grid data and adjust grid dimensions
        self.m_grid7.ClearGrid()

        # Adjust the grid's rows and columns based on the filtered data
        current_rows = self.m_grid7.GetNumberRows()
        current_cols = self.m_grid7.GetNumberCols()

        if current_rows < rows:
            self.m_grid7.AppendRows(rows - current_rows)
        elif current_rows > rows:
            self.m_grid7.DeleteRows(0, current_rows - rows)

        if current_cols < cols:
            self.m_grid7.AppendCols(cols - current_cols)
        elif current_cols > cols:
            self.m_grid7.DeleteCols(0, current_cols - cols)

        # Set column labels
        for col_idx, col_label in enumerate(data_frame.columns):
            self.m_grid7.SetColLabelValue(col_idx, col_label)

        # Set the values in the grid
        for row_idx in range(rows):
            for col_idx in range(cols):
                self.m_grid7.SetCellValue(row_idx, col_idx, str(data_frame.iat[row_idx, col_idx]))

    def clear_results(self):
        """Clears the results from the grid."""
        # Clear all the grid data without removing rows/columns
        self.m_grid7.ClearGrid()

        # Delete extra rows and columns
        current_rows = self.m_grid7.GetNumberRows()
        current_cols = self.m_grid7.GetNumberCols()

        if current_rows > 0:
            self.m_grid7.DeleteRows(0, current_rows)

        if current_cols > 0:
            self.m_grid7.DeleteCols(0, current_cols)

    def food_search_reset(self):
        """Resets the UI values to how it was when we first opened the Food Search page."""
        # Clear any search results displayed in the grid
        self.clear_results()

        # Reset any other components if needed (e.g., dropdowns)
        self.m_choice3.SetSelection(-1)  # Reset nutrition type dropdown
        self.m_choice4.SetSelection(-1)  # Reset nutrition level dropdown

        # Refresh the layout after resetting
        self.Layout()
