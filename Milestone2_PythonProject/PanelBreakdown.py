import wx
import matplotlib.pyplot as plt
from template_breakdown_panel import NutritionBreakdownPanel
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from all_functions import *

class PanelNutritionBreakdown(NutritionBreakdownPanel):
    def __init__(self, parent):
        super().__init__(parent)
        self.df = get_data('Food_Nutrition_Dataset.csv')
        self.df.iloc[:, 1:] = self.df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    
    def NB_OnSearch(self, event):
        self.NB_chart_panel.DestroyChildren()
        self.NB_caloric_value_text = None
        self.NB_nutrition_density_text = None
        self.NB_search_text = None
        self.NB_result_text = None
        self.NB_caloric_value_text.Hide()
        self.NB_nutrition_density_text.Hide()
        self.NB_result_text.Hide()

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
                names = list(major_nutrients.keys())
                values = list(major_nutrients.values())

                # Pie chart
                ax1.pie(values, labels=names, autopct='%1.1f%%', startangle=90, shadow=True)
                ax1.set_title(f"Pie Chart for {food_name}'s nutrition values")

                # Bar graph
                ax2.bar(names, values, color='skyblue')
                ax2.set_xlabel('Nutrients')
                ax2.set_ylabel('Values')
                ax2.set_title(f"Bar Graph for {food_name}'s nutrition values")
                ax2.set_xticks(range(len(names)))
                ax2.set_xticklabels(names, rotation=90)

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

    def NB_reset(self):
        self.NB_chart_panel.DestroyChildren()
        self.NB_caloric_value_text = None
        self.NB_nutrition_density_text = None
        self.NB_search_text = None
        self.NB_result_text = None

    def go_to_main(self, event):
        self.RF_reset()
        self.GetParent().go_to_main()
