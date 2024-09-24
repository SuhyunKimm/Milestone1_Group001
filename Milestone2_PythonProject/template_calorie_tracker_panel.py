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

        ct_sub_sizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.ct_amount_label = wx.StaticText( self, wx.ID_ANY, _(u"Daily intake calorie :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ct_amount_label.Wrap( -1 )

        ct_sub_sizer1.Add( self.ct_amount_label, 0, wx.ALL, 5 )

        self.calorie_label = wx.StaticText( self, wx.ID_ANY, _(u"1500 (kcal)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.calorie_label.Wrap( -1 )

        ct_sub_sizer1.Add( self.calorie_label, 0, wx.ALL, 5 )


        calorie_tracker_sizer1.Add( ct_sub_sizer1, 0, wx.EXPAND, 5 )

        ct_sub_sizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_slider1 = wx.Slider( self, wx.ID_ANY, 1500, 0, 3000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        ct_sub_sizer2.Add( self.m_slider1, 1, wx.ALL|wx.EXPAND, 5 )


        calorie_tracker_sizer1.Add( ct_sub_sizer2, 0, wx.EXPAND, 5 )

        ct_sub_sizer3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        ct_sub_sizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.search_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        ct_sub_sizer4.Add( self.search_box, 1, wx.ALL|wx.EXPAND, 5 )

        self.search_btn = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        ct_sub_sizer4.Add( self.search_btn, 0, wx.ALL, 5 )


        bSizer15.Add( ct_sub_sizer4, 0, wx.EXPAND, 5 )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        search_food_listChoices = [ _(u"No Data") ]
        self.search_food_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, search_food_listChoices, 0 )
        bSizer16.Add( self.search_food_list, 1, wx.ALL|wx.EXPAND, 5 )

        self.food_select_btn = wx.Button( self, wx.ID_ANY, _(u"Select"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.food_select_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )


        ct_sub_sizer3.Add( bSizer15, 1, wx.EXPAND, 5 )

        ct_sub_sizer5 = wx.BoxSizer( wx.VERTICAL )

        self.tracker_graph_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        ct_sub_sizer5.Add( self.tracker_graph_panel, 2, wx.EXPAND |wx.ALL, 5 )


        ct_sub_sizer3.Add( ct_sub_sizer5, 1, wx.EXPAND, 5 )


        calorie_tracker_sizer1.Add( ct_sub_sizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( calorie_tracker_sizer1 )
        self.Layout()

        # Connect Events
        self.m_slider1.Bind( wx.EVT_SCROLL, self.slider_change_value )
        self.search_btn.Bind( wx.EVT_BUTTON, self.search_btn_clicked )
        self.search_food_list.Bind( wx.EVT_LISTBOX, self.chose_food_item )
        self.food_select_btn.Bind( wx.EVT_BUTTON, self.select_food )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def slider_change_value( self, event ):
        event.Skip()

    def search_btn_clicked( self, event ):
        event.Skip()

    def chose_food_item( self, event ):
        event.Skip()

    def select_food( self, event ):
        event.Skip()


