import wx
import pandas as pd
from level_filter_all_functions import filter_by_nutrition_and_level, df
from template_main_panel import MainPanel
from template_level_filter_panel import MyPanel2

class PanelLevelFilter(MyPanel2):
    def __init__(self, parent):
        super().__init__(parent)

        # Populate choices for the dropdown menus
        self.m_choice3.SetItems(list(df.columns))  # Set items for nutrition type
        self.m_choice4.SetItems(["low", "mid", "high"])  # Set items for nutrition level

    def level_filter_go_back_btn_click(self, event):
        """Handles the Go Back button click."""
        print("Go Back button clicked!")
        self.GetParent().go_to_main()

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

        # Filter the DataFrame based on the selected nutrition type and level
        filtered_df = filter_by_nutrition_and_level(nutrition_type, nutrition_level)

        # Handle the case where no matches are found or display the filtered data
        if isinstance(filtered_df, str):
            wx.MessageBox(filtered_df, "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            self.populate_grid(filtered_df)

    def populate_grid(self, data_frame):
        """Populates the wx.Grid with the data from the filtered DataFrame."""
        rows, cols = data_frame.shape

        # Clear existing grid data and adjust grid dimensions
        self.m_grid7.ClearGrid()

        # Adjust rows and columns
        current_rows = self.m_grid7.GetNumberRows()
        current_cols = self.m_grid7.GetNumberCols()

        # Adjust the grid's rows and columns based on the filtered data
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
