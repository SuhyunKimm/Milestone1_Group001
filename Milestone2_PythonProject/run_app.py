import wx
import wx.grid

from template_frame import MyFrame
from PanelMain import PanelMain
from PanelFoodSearch import PanelFoodSearch
from PanelBreakdown import PanelBreakdown
from PanelRangeFilter import PanelRangeFilter
from PanelLevelFilter import PanelLevelFilter
from PanelTracker import PanelCalorieTracker

class Frame(MyFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize panels
        self.panel_main = PanelMain(self)
        self.panel_search = PanelFoodSearch(self)
        self.panel_breakdown = PanelBreakdown(self)
        self.panel_rfilter = PanelRangeFilter(self)
        self.panel_lfilter = PanelLevelFilter(self)
        self.panel_tracker = PanelCalorieTracker(self)

        self.panel_list = [self.panel_main, self.panel_search, self.panel_breakdown, self.panel_rfilter, self.panel_lfilter,
                      self.panel_tracker]
        self.current_panel = 0

        for i in range(1,len(self.panel_list)) :
            self.panel_list[i].Hide()

        # Add panels to the sizer
        for i in range(len(self.panel_list)) :
            self.main_sizer.Add(self.panel_list[i], 1, wx.EXPAND)

        self.Layout()

    def reset_food_search_panel(self):
        pass

    def reset_breakdown_panel(self):
        pass

    def reset_range_filter_panel(self):
        pass

    def reset_level_filter_panel(self):
        pass

    def close_current_panel(self, i):
        if i == 1 :
            self.reset_food_search_panel()
        elif i == 2 :
            self.reset_breakdown_panel()
        elif i == 3 :
            self.reset_range_filter_panel()
        elif i == 4 :
            self.reset_level_filter_panel()
        elif i == 5 :
            self.panel_tracker.tracker_reset()
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
