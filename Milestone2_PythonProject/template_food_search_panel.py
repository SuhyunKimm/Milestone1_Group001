# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-43-gf15ce330)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyPanel2
###########################################################################

class FoodSearchPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.food_search_go_back_btn = wx.Button( self, wx.ID_ANY, _(u"Go Back"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer1.Add( self.food_search_go_back_btn, 0, wx.ALL, 5 )


        bSizer6.Add( wSizer1, 0, wx.EXPAND, 5 )

        wSizer2 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Enter a food name:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        wSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer2.Add( self.m_textCtrl5, 1, wx.ALL, 5 )

        self.food_search_search_btn = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        wSizer2.Add( self.food_search_search_btn, 0, wx.ALL, 5 )


        bSizer6.Add( wSizer2, 0, wx.EXPAND, 5 )

        self.m_grid7 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid7.CreateGrid( 5, 5 )
        self.m_grid7.EnableEditing( True )
        self.m_grid7.EnableGridLines( True )
        self.m_grid7.EnableDragGridSize( False )
        self.m_grid7.SetMargins( 0, 0 )

        # Columns
        self.m_grid7.EnableDragColMove( False )
        self.m_grid7.EnableDragColSize( True )
        self.m_grid7.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid7.EnableDragRowSize( True )
        self.m_grid7.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid7.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer6.Add( self.m_grid7, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.food_search_go_back_btn.Bind( wx.EVT_BUTTON, self.food_search_go_back_btn_click )
        self.food_search_search_btn.Bind( wx.EVT_BUTTON, self.food_search_search_btn_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def food_search_go_back_btn_click( self, event ):
        event.Skip()

    def food_search_search_btn_click( self, event ):
        event.Skip()
