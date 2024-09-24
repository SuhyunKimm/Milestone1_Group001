import wx
import wx.grid

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

from template_frame import MyFrame
from template_main_panel import MainPanel
from template_calorie_tracker_panel import CalorieTrackerPanel
from tracker_all_functions import *

df = get_data('')
class Panel_CalorieTracker(CalorieTrackerPanel):
    def __init__(self, parent):
        self.cal_val = 1500
        self.selected_food_name = ['Unconsumed']
        self.selected_food_cal = [self.cal_val]
        self.searched_df = None
        self.selected_item = None

        super().__init__(parent)

    def goback( self, event ):
        self.GetParent().go_to_main()

    def slider_change_value( self, event ):
        self.get_slider_val()
        self.calorie_label.SetLabel(f'{self.cal_val} (kcal)')

    def get_slider_val(self):
        self.cal_val = self.m_slider1.GetValue()

    def set_cal_label(self):
        self.calorie_label.SetLabel(f'{self.cal_val} (kcal)')

    def search_btn_clicked( self, event ):
        search_txt = self.search_box.GetValue()
        self.searched_df = search_food_by_name(df, search_txt)
        processed_list = get_food_name_and_calorie(self.searched_df)
        self.search_food_list.Set(processed_list)

    def chose_food_item( self, event ):
        self.selected_item = self.searched_df.iloc[self.search_food_list.GetSelection()]

    def select_food( self, event ):
        self.selected_food_name.insert(-2,self.selected_item['food'])
        self.selected_food_cal.insert(-2,self.selected_item['Caloric Value'])
        self.selected_food_cal[-1] -= self.selected_item['Caloric Value']
        print(self.selected_food_name)
        print(self.selected_food_cal)
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

class Panel_Main(MainPanel):
    def __init__(self, parent):
        super().__init__(parent)

    def btn_food_search_clicked(self, event):
        self.GetParent().go_to_search()

    def btn_nutritional_breakdown_clicked(self, event):
        self.GetParent().go_to_bd()

    def btn_range_filter_clicked(self, event):
        self.GetParent().go_to_rfilter()

    def btn_level_filter_clicked(self, event):
        self.GetParent().go_to_lfilter()

    def btn_tracker_clicked(self, event):
        self.GetParent().go_to_tracker()


class Frame(MyFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize panels
        self.panel_main = Panel_Main(self)
        self.panel_search = Panel_CalorieTracker(self)
        self.panel_breakdown = Panel_CalorieTracker(self)
        self.panel_rfilter = Panel_CalorieTracker(self)
        self.panel_lfilter = Panel_CalorieTracker(self)
        self.panel_tracker = Panel_CalorieTracker(self)

        self.panel_list = [self.panel_main, self.panel_search, self.panel_breakdown, self.panel_rfilter, self.panel_lfilter,
                      self.panel_tracker]
        self.current_panel = 0

        for i in range(1,len(self.panel_list)) :
            self.panel_list[i].Hide()

        # Add panels to the sizer
        for i in range(len(self.panel_list)) :
            self.main_sizer.Add(self.panel_list[i], 1, wx.EXPAND)

        self.Layout()

    def close_current_panel(self, i):
        self.panel_list[i].Hide()
    def go_to_main(self):
        self.close_current_panel(self.current_panel)
        self.panel_main.Show()
        self.current_panel = 0
        self.Layout()

    def go_to_search(self):
        self.current_panel = 1
        self.panel_main.Hide()
        self.panel_search.Show()
        self.Layout()

    def go_to_bd(self):
        self.current_panel = 2
        self.panel_main.Hide()
        self.panel_breakdown.Show()
        self.Layout()

    def go_to_rfilter(self):
        self.current_panel = 3
        self.panel_main.Hide()
        self.panel_rfilter.Show()
        self.Layout()

    def go_to_lfilter(self):
        self.current_panel = 4
        self.panel_main.Hide()
        self.panel_lfilter.Show()
        self.Layout()

    def go_to_tracker(self):
        self.current_panel = 5
        self.panel_main.Hide()
        self.panel_tracker.Show()
        self.Layout()

if __name__ == "__main__":
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
