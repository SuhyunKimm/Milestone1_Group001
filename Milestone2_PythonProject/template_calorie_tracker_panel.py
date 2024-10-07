# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class CalorieTrackerPanel
###########################################################################

class CalorieTrackerPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        calorie_tracker_sizer1 = wx.BoxSizer( wx.VERTICAL )

        tracker_go_back_btn_sizer = wx.BoxSizer( wx.VERTICAL )

        self.tracker_go_back_btn = wx.Button( self, wx.ID_ANY, _(u"Go Back"), wx.DefaultPosition, wx.DefaultSize, 0 )
        tracker_go_back_btn_sizer.Add( self.tracker_go_back_btn, 0, wx.ALL, 5 )


        calorie_tracker_sizer1.Add( tracker_go_back_btn_sizer, 0, wx.EXPAND, 5 )

        tracker_sub_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.tracker_amount_label = wx.StaticText( self, wx.ID_ANY, _(u"Daily intake calorie :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.tracker_amount_label.Wrap( -1 )

        tracker_sub_sizer1.Add( self.tracker_amount_label, 0, wx.ALL, 5 )

        self.tracker_calorie_label = wx.StaticText( self, wx.ID_ANY, _(u"1500 (kcal)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.tracker_calorie_label.Wrap( -1 )

        tracker_sub_sizer1.Add( self.tracker_calorie_label, 0, wx.ALL, 5 )


        calorie_tracker_sizer1.Add( tracker_sub_sizer1, 0, wx.EXPAND, 5 )

        tracker_sub_sizer2 = wx.BoxSizer( wx.VERTICAL )

        self.tracker_slider1 = wx.Slider( self, wx.ID_ANY, 1500, 0, 3000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        tracker_sub_sizer2.Add( self.tracker_slider1, 1, wx.ALL|wx.EXPAND, 5 )


        calorie_tracker_sizer1.Add( tracker_sub_sizer2, 0, wx.EXPAND, 5 )

        tracker_sub_sizer3 = wx.BoxSizer( wx.HORIZONTAL )

        tracker_bSizer15 = wx.BoxSizer( wx.VERTICAL )

        tracker_sub_sizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.tracker_search_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        tracker_sub_sizer4.Add( self.tracker_search_box, 1, wx.ALL|wx.EXPAND, 5 )

        self.tracker_search_btn = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        tracker_sub_sizer4.Add( self.tracker_search_btn, 0, wx.ALL, 5 )


        tracker_bSizer15.Add( tracker_sub_sizer4, 0, wx.EXPAND, 5 )

        tracker_bSizer16 = wx.BoxSizer( wx.VERTICAL )

        tracker_search_food_listChoices = [ _(u"No Data") ]
        self.tracker_search_food_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, tracker_search_food_listChoices, 0 )
        tracker_bSizer16.Add( self.tracker_search_food_list, 1, wx.ALL|wx.EXPAND, 5 )

        self.tracker_food_select_btn = wx.Button( self, wx.ID_ANY, _(u"Select"), wx.DefaultPosition, wx.DefaultSize, 0 )
        tracker_bSizer16.Add( self.tracker_food_select_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        tracker_bSizer15.Add( tracker_bSizer16, 1, wx.EXPAND, 5 )


        tracker_sub_sizer3.Add( tracker_bSizer15, 1, wx.EXPAND, 5 )

        tracker_sub_sizer5 = wx.BoxSizer( wx.VERTICAL )

        self.tracker_graph_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        tracker_sub_sizer5.Add( self.tracker_graph_panel, 2, wx.EXPAND |wx.ALL, 5 )


        tracker_sub_sizer3.Add( tracker_sub_sizer5, 1, wx.EXPAND, 5 )


        calorie_tracker_sizer1.Add( tracker_sub_sizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( calorie_tracker_sizer1 )
        self.Layout()

        # Connect Events
        self.tracker_go_back_btn.Bind( wx.EVT_BUTTON, self.tracker_go_back_btn_clicked )
        self.tracker_slider1.Bind( wx.EVT_SCROLL, self.tracker_slider_change_value )
        self.tracker_search_btn.Bind( wx.EVT_BUTTON, self.tracker_search_btn_clicked )
        self.tracker_search_food_list.Bind( wx.EVT_LISTBOX, self.tracker_chose_food_item )
        self.tracker_food_select_btn.Bind( wx.EVT_BUTTON, self.tracker_select_food )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def tracker_go_back_btn_clicked( self, event ):
        event.Skip()

    def tracker_slider_change_value( self, event ):
        event.Skip()

    def tracker_search_btn_clicked( self, event ):
        event.Skip()

    def tracker_chose_food_item( self, event ):
        event.Skip()

    def tracker_select_food( self, event ):
        event.Skip()

