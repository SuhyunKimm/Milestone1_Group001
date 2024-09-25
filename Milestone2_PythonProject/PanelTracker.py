from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from template_calorie_tracker_panel import CalorieTrackerPanel
from tracker_all_functions import *
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt

class PanelCalorieTracker(CalorieTrackerPanel):
    def __init__(self, parent):
        self.cal_val = 1500
        self.selected_food_name = ['Unconsumed']
        self.selected_food_cal = [self.cal_val]
        self.searched_df = None
        self.selected_item = None
        self.df = get_data('Food_Nutrition_Dataset.csv')
        super().__init__(parent)

    def tracker_reset(self):
        self.cal_val = 1500
        self.selected_food_name = ['Unconsumed']
        self.selected_food_cal = [self.cal_val]
        self.searched_df = None
        self.selected_item = None
        self.tracker_slider1.SetValue(1500)
        self.tracker_calorie_label.SetLabel('1500 (kcal)')
        self.tracker_graph_panel.DestroyChildren()
        self.tracker_graph_panel.Layout()
        self.tracker_search_box.SetValue('')
        self.tracker_search_food_list.Clear()


    def tracker_go_back_btn_clicked(self, event):
        self.GetParent().go_to_main()

    def tracker_slider_change_value(self, event):
        self.tracker_get_slider_val()
        self.tracker_calorie_label.SetLabel(f'{self.cal_val} (kcal)')

    def tracker_get_slider_val(self):
        self.cal_val = self.tracker_slider1.GetValue()

    def tracker_search_btn_clicked(self, event):
        search_txt = self.tracker_search_box.GetValue()
        self.searched_df = search_food_by_name(self.df, search_txt)
        processed_list = get_food_name_and_calorie(self.searched_df)
        self.tracker_search_food_list.Set(processed_list)

    def tracker_chose_food_item(self, event):
        self.selected_item = self.searched_df.iloc[self.tracker_search_food_list.GetSelection()]

    def tracker_select_food(self, event):
        if self.selected_item['Caloric Value'] <= self.selected_food_cal[-1] :
            self.selected_food_name.insert(-2, self.selected_item['food'])
            self.selected_food_cal.insert(-2, self.selected_item['Caloric Value'])
            self.selected_food_cal[-1] -= self.selected_item['Caloric Value']
            figure_score = self.plot_data_pie()
            h,w = self.tracker_graph_panel.GetSize()
            figure_score.set_size_inches(h / figure_score.get_dpi(), w / figure_score.get_dpi())
            canvas = FigureCanvasWxAgg(self.tracker_graph_panel, -1, figure_score)
            canvas.SetSize(self.tracker_graph_panel.GetSize())
            self.Layout()

    def plot_data_pie(self) :
        figure_score, ax = plt.subplots(1,1)
        ax.pie(self.selected_food_cal, labels=self.selected_food_name, autopct="%.1f%%", shadow=True)
        ax.axis('equal')
        return figure_score
