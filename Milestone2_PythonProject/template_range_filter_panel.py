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
## Class NutritionRangeFilterPanel
###########################################################################

class NutritionRangeFilterPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        RF_vbox = wx.BoxSizer( wx.VERTICAL )

        RF_top_row = wx.BoxSizer( wx.HORIZONTAL )

        self.RF_go_back_btn = wx.Button( self, wx.ID_ANY, _(u"Back"), wx.DefaultPosition, wx.DefaultSize, 0 )
        RF_top_row.Add( self.RF_go_back_btn, 0, wx.ALL, 5 )

        self.RF_title = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Range Filter"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.RF_title.Wrap( -1 )

        self.RF_title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        RF_top_row.Add( self.RF_title, 1, wx.ALL, 5 )


        RF_vbox.Add( RF_top_row, 0, wx.EXPAND, 5 )

        RF_search_box = wx.BoxSizer( wx.HORIZONTAL )

        RF_nutrient_choiceChoices = []
        self.RF_nutrient_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, RF_nutrient_choiceChoices, wx.CB_SORT )
        self.RF_nutrient_choice.SetSelection( 0 )
        RF_search_box.Add( self.RF_nutrient_choice, 1, wx.ALL, 5 )


        RF_vbox.Add( RF_search_box, 0, wx.EXPAND, 5 )

        RF_slider_box = wx.BoxSizer( wx.HORIZONTAL )

        self.RF_min_label = wx.StaticText( self, wx.ID_ANY, _(u"Min:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RF_min_label.Wrap( -1 )

        RF_slider_box.Add( self.RF_min_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.RF_min_slider = wx.Slider( self, wx.ID_ANY, 0, 0, 550, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        RF_slider_box.Add( self.RF_min_slider, 1, wx.ALL, 5 )

        self.RF_min_value_static = wx.StaticText( self, wx.ID_ANY, _(u"0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RF_min_value_static.Wrap( -1 )

        RF_slider_box.Add( self.RF_min_value_static, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        RF_slider_box.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.RF_max_label = wx.StaticText( self, wx.ID_ANY, _(u"Max:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RF_max_label.Wrap( -1 )

        RF_slider_box.Add( self.RF_max_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.RF_max_slider = wx.Slider( self, wx.ID_ANY, 100, 0, 600, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        RF_slider_box.Add( self.RF_max_slider, 1, wx.ALL, 5 )

        self.RF_max_value_static = wx.StaticText( self, wx.ID_ANY, _(u"100"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.RF_max_value_static.Wrap( -1 )

        RF_slider_box.Add( self.RF_max_value_static, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        RF_vbox.Add( RF_slider_box, 0, wx.EXPAND, 5 )

        RF_button_box = wx.BoxSizer( wx.HORIZONTAL )

        self.RF_filter_btn = wx.Button( self, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        RF_button_box.Add( self.RF_filter_btn, 0, wx.ALL, 5 )


        RF_vbox.Add( RF_button_box, 0, wx.ALIGN_CENTER, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.RF_result = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.BORDER_SUNKEN )
        bSizer6.Add( self.RF_result, 1, wx.ALL|wx.EXPAND, 5 )


        RF_vbox.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.SetSizer( RF_vbox )
        self.Layout()

        # Connect Events
        self.RF_go_back_btn.Bind( wx.EVT_BUTTON, self.go_to_main )
        self.RF_nutrient_choice.Bind( wx.EVT_CHOICE, self.RF_OnChoose )
        self.RF_min_slider.Bind( wx.EVT_SLIDER, self.OnSliderUpdate )
        self.RF_max_slider.Bind( wx.EVT_SLIDER, self.OnSliderUpdate )
        self.RF_filter_btn.Bind( wx.EVT_BUTTON, self.RF_OnFilter )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def go_to_main( self, event ):
        event.Skip()

    def RF_OnChoose( self, event ):
        event.Skip()

    def OnSliderUpdate( self, event ):
        event.Skip()


    def RF_OnFilter( self, event ):
        event.Skip()


