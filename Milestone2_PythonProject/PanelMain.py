from template_main_panel import MainPanel

class PanelMain(MainPanel):
    def __init__(self, parent):
        super().__init__(parent)

    def main_btn_food_search_clicked(self, event):
        self.GetParent().go_to_search()

    def main_btn_nutritional_breakdown_clicked(self, event):
        self.GetParent().go_to_bd()

    def main_btn_range_filter_clicked(self, event):
        self.GetParent().go_to_rfilter()

    def main_btn_level_filter_clicked(self, event):
        self.GetParent().go_to_lfilter()

    def main_btn_tracker_clicked(self, event):
        self.GetParent().go_to_tracker()
