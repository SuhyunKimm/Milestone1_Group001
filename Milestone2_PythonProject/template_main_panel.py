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
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,303 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        main_panel_sizer = wx.BoxSizer( wx.VERTICAL )

        self.main_panel_text1 = wx.StaticText( self, wx.ID_ANY, _(u"Welcome to Nutrition Analysis and Tracking Application!"), wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.main_panel_text1.Wrap( -1 )

        main_panel_sizer.Add( self.main_panel_text1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )

        main_panel_btn_sizer = wx.BoxSizer( wx.VERTICAL )

        self.main_btn_food_search = wx.Button( self, wx.ID_ANY, _(u"Food Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        main_panel_btn_sizer.Add( self.main_btn_food_search, 0, wx.ALL|wx.EXPAND, 10 )

        self.main_btn_nutritional_breakdown = wx.Button( self, wx.ID_ANY, _(u"Nutritional Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        main_panel_btn_sizer.Add( self.main_btn_nutritional_breakdown, 0, wx.ALL|wx.EXPAND, 10 )

        self.main_btn_nutrition_range_filter = wx.Button( self, wx.ID_ANY, _(u"Nutrition Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        main_panel_btn_sizer.Add( self.main_btn_nutrition_range_filter, 0, wx.ALL|wx.EXPAND, 10 )

        self.main_btn_nutrition_level_filter = wx.Button( self, wx.ID_ANY, _(u"Nutrition Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        main_panel_btn_sizer.Add( self.main_btn_nutrition_level_filter, 0, wx.ALL|wx.EXPAND, 10 )

        self.main_btn_nutrition_tracker = wx.Button( self, wx.ID_ANY, _(u"Nutrition Tracker"), wx.DefaultPosition, wx.DefaultSize, 0 )
        main_panel_btn_sizer.Add( self.main_btn_nutrition_tracker, 0, wx.ALL|wx.EXPAND, 10 )


        main_panel_sizer.Add( main_panel_btn_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( main_panel_sizer )
        self.Layout()

        # Connect Events
        self.main_btn_food_search.Bind( wx.EVT_BUTTON, self.main_btn_food_search_clicked )
        self.main_btn_nutritional_breakdown.Bind( wx.EVT_BUTTON, self.main_btn_nutritional_breakdown_clicked )
        self.main_btn_nutrition_range_filter.Bind( wx.EVT_BUTTON, self.main_btn_range_filter_clicked )
        self.main_btn_nutrition_level_filter.Bind( wx.EVT_BUTTON, self.main_btn_level_filter_clicked )
        self.main_btn_nutrition_tracker.Bind( wx.EVT_BUTTON, self.main_btn_tracker_clicked )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def main_btn_food_search_clicked( self, event ):
        event.Skip()

    def main_btn_nutritional_breakdown_clicked( self, event ):
        event.Skip()

    def main_btn_range_filter_clicked( self, event ):
        event.Skip()

    def main_btn_level_filter_clicked( self, event ):
        event.Skip()

    def main_btn_tracker_clicked( self, event ):
        event.Skip()


