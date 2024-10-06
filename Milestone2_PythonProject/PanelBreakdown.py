#from template_breakdown_panel import BreakdownPanel
from template_main_panel import MainPanel
import wx
import matplotlib.pyplot as plt
from template_breakdown_panel import NutritionBreakdownPanel
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from breakdown_all_functions import *

class PanelNutritionBreakdown(NutritionBreakdownPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.df = load_data('Food_Nutrition_Dataset.csv')
        self.canvas = None
    
    def NB_OnSearch(self, event):
        clear_previous_data(self.canvas, self.NB_caloric_value_text, self.NB_nutrition_density_text, self.NB_result_text)

        NB_search_text = self.NB_search_text.GetValue().strip()

        if NB_search_text:
            matches = search_food(self.df, NB_search_text)

            if not matches.empty:
                result = matches.iloc[0]
                food_name = result['food'].title()
                nutrients = extract_nutrient_info(result)

                major_nutrients = prepare_nutrients(nutrients)

                caloric_value = result.iloc[1]  
                nutrition_density = result.iloc[-1]  

                self.NB_caloric_value_text.SetLabel(f"Caloric Value: {caloric_value}")
                self.NB_nutrition_density_text.SetLabel(f"Nutrition Density: {nutrition_density}")

                self.NB_caloric_value_text.Show()
                self.NB_nutrition_density_text.Show()

                fig, axes = plt.subplots(1, 2)
                ax1, ax2 = axes
                plot_nutrients(major_nutrients, food_name, ax1, ax2)

                fig.tight_layout()
                h, w = self.NB_chart_panel.GetSize()
                fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
                self.canvas = FigureCanvas(self.NB_chart_panel, -1, fig)
                self.canvas.SetSize((h, w))

            else:
                self.NB_result_text.SetLabel(f'No data found for "{self.NB_search_text.GetValue()}"')
                self.NB_result_text.Show()
        else:
            self.NB_result_text.SetLabel("Please enter a food name to search.")
            self.NB_result_text.Show()

        self.Layout()

if __name__ == "__main__":
    app = wx.App(False)
    frame = wx.Frame(None, title="Nutrition Breakdown", size=(800, 600))
    panel = PanelNutritionBreakdown(frame)
    frame.Show(True)
    app.MainLoop()
