import wx
import math
from template_range_filter_panel import NutritionRangeFilterPanel
from all_functions import *


class PanelRangeFilter(NutritionRangeFilterPanel):
    def __init__(self, parent):
        super().__init__(parent)

        # self.df = load_data(r'.\\UI-design-test\\Food_Nutrition_Dataset.csv')
        self.df = load_data('Food_Nutrition_Dataset.csv')
        self.RF_filter_btn.Bind(wx.EVT_BUTTON, self.RF_OnFilter)

        self.RF_result.InsertColumn(0, "Food name", width=wx.LIST_AUTOSIZE_USEHEADER)

        self.RF_nutrient_choiceChoices = list(self.df.columns[1:].values)  # append the nutrient choices to the dropbox
        self.RF_nutrient_choice.SetItems(self.RF_nutrient_choiceChoices)

    def go_to_main(self, event):
        self.GetParent().go_to_main()

    def RF_OnChoose(self, event):
        self.RF_nutrient_name = self.RF_nutrient_choice.GetStringSelection()

        RF_nutrient_min_value = math.ceil(min(self.df[self.RF_nutrient_name]))
        RF_nutrient_max_value = math.ceil(max(self.df[self.RF_nutrient_name]))

        self.RF_max_slider.SetMin(RF_nutrient_min_value)
        self.RF_max_slider.SetMax(RF_nutrient_max_value)
        self.RF_max_slider.SetValue(RF_nutrient_max_value)

        self.RF_min_slider.SetMin(RF_nutrient_min_value)
        self.RF_min_slider.SetMax(RF_nutrient_max_value)
        self.RF_min_slider.SetValue(RF_nutrient_min_value)

        self.Layout()

    def OnSliderUpdate(self, event):

        self.RF_min_value_static.SetLabel(str(self.RF_min_slider.GetValue()))
        if self.RF_max_slider.GetValue() < self.RF_min_slider.GetValue():
            self.RF_max_slider.SetValue(self.RF_min_slider.GetValue())
        self.RF_max_value_static.SetLabel(str(self.RF_max_slider.GetValue()))
        self.Layout()

    def RF_OnFilter(self, event):

        RF_min_value = self.RF_min_slider.GetValue()
        RF_max_value = self.RF_max_slider.GetValue()

        food_list, message = filter_foods_by_nutrient(self.df, self.RF_nutrient_name, RF_min_value, RF_max_value)

        self.RF_result.DeleteAllItems()

        if food_list:
            for i, food in enumerate(food_list):
                self.RF_result.InsertItem(i, food.title())  # Add items to ListCtrl
        else:
            self.RF_result.InsertItem(0, message)  # Display message if no results found

        self.Layout()


if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="Nutrition Range Filter", size=(800, 600))
    panel = PanelRangeFilter(frame)
    frame.Show(True)
    app.MainLoop()
