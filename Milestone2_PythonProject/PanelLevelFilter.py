import pandas as pd

from level_filter_all_functions import df
from template_main_panel import MainPanel
import wx
from template_level_filter_panel import MyPanel2

class PanelLevelFilter(MyPanel2):
    def __init__(self, parent):
        super().__init__(parent)
        self.m_choice3 = wx.ComboBox(self, choices=list(df.columns), style=wx.CB_READONLY)





    def nutrition_type_choice(self, event):
        """Override Nutrition type choice."""
        selected_nutrition_type = self.m_choice3.GetValue()

    def nutrition_level_choice(self, event):
        """Override Nutrition level choice."""
        selected_nutrition_level = self.m_choice4.GetValue()


    def level_filter_go_back_btn_click(self, event):
        """Handles the Go Back button click."""
        print("Go Back button clicked!")
        self.GetParent().go_to_main()

    def level_filter_search_btn_click(self, event):
        """Override Search button click."""
        nutrition_type = self.nutrition_type_combobox.GetValue()
        nutrition_level = self.nutrition_level_combobox.GetValue()

        if not nutrition_type or not nutrition_level:
            wx.MessageBox("Please select both nutrition type and nutrition level.", "Info", wx.OK | wx.ICON_INFORMATION)
            return

        # Convert nutrition level to an integer (index is zero-based)
        level_index = int(nutrition_level) - 1

        # Filter DataFrame based on selected nutrition type and level
        if nutrition_type in df.columns and level_index < len(df):
            filtered_data = df[[nutrition_type]].iloc[[level_index]]
            self.populate_grid(filtered_data)
        else:
            wx.MessageBox("Invalid selection. Please try again.", "Error", wx.OK | wx.ICON_ERROR)

    def populate_grid(self, data_frame):
        """Populates the wx.Grid with the data from the DataFrame."""
        rows, cols = data_frame.shape

        # Clear the grid and recreate it with the new size
        self.m_grid7.ClearGrid()
        if self.m_grid7.GetNumberRows() > 0:
            self.m_grid7.DeleteRows(0, self.grid.GetNumberRows())
        if self.m_grid7.GetNumberCols() > 0:
            self.m_grid7.DeleteCols(0, self.grid.GetNumberCols())

        self.m_grid7.CreateGrid(rows, cols)

        # Set column labels
        for col_idx, col_label in enumerate(data_frame.columns):
            self.m_grid7.SetColLabelValue(col_idx, col_label)

        # Set the values in the grid
        for row_idx in range(rows):
            for col_idx in range(cols):
                self.m_grid7.SetCellValue(row_idx, col_idx, str(data_frame.iat[row_idx, col_idx]))