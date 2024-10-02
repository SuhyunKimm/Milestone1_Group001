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
## Class NutritionBreakdownPanel
###########################################################################

class NutritionBreakdownPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        NB_vbox = wx.BoxSizer( wx.VERTICAL )

        NB_top_row = wx.BoxSizer( wx.HORIZONTAL )

        self.NB_go_to_main_btn = wx.Button( self, wx.ID_ANY, _(u"Back"), wx.DefaultPosition, wx.DefaultSize, 0 )
        NB_top_row.Add( self.NB_go_to_main_btn, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Breakdown"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        NB_top_row.Add( self.m_staticText4, 1, wx.ALL, 5 )


        NB_vbox.Add( NB_top_row, 0, wx.EXPAND, 5 )


        NB_vbox.Add( ( 0, 10), 0, 0, 0 )

        NB_search_box = wx.BoxSizer( wx.HORIZONTAL )

        self.NB_search_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        NB_search_box.Add( self.NB_search_text, 1, wx.ALL, 5 )

        self.NB_search_btn = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        NB_search_box.Add( self.NB_search_btn, 0, wx.ALL, 5 )


        NB_vbox.Add( NB_search_box, 0, wx.EXPAND, 5 )

        self.NB_nutrition_density_text = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Density: N/A"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NB_nutrition_density_text.Wrap( -1 )

        self.NB_nutrition_density_text.Hide()

        NB_vbox.Add( self.NB_nutrition_density_text, 0, wx.ALL, 5 )

        self.NB_caloric_value_text = wx.StaticText( self, wx.ID_ANY, _(u"Caloric Value: N/A"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NB_caloric_value_text.Wrap( -1 )

        self.NB_caloric_value_text.Hide()

        NB_vbox.Add( self.NB_caloric_value_text, 0, wx.ALL, 5 )

        self.NB_result_text = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NB_result_text.Wrap( -1 )

        self.NB_result_text.Hide()

        NB_vbox.Add( self.NB_result_text, 0, wx.ALL, 5 )

        self.NB_chart_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        NB_chart_sizer = wx.BoxSizer( wx.HORIZONTAL )


        self.NB_chart_panel.SetSizer( NB_chart_sizer )
        self.NB_chart_panel.Layout()
        NB_chart_sizer.Fit( self.NB_chart_panel )
        NB_vbox.Add( self.NB_chart_panel, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( NB_vbox )
        self.Layout()

        # Connect Events
        self.NB_go_to_main_btn.Bind( wx.EVT_BUTTON, self.go_to_main )
        self.NB_search_btn.Bind( wx.EVT_BUTTON, self.NB_OnSearch )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def go_to_main( self, event ):
        event.Skip()

    def NB_OnSearch( self, event ):
        event.Skip()


