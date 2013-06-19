# encoding: utf-8
#
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
from kivy.graphics import *
from kivy.properties import *

class FixHeaderAndFooterLayout( Layout ):
    def __init__( self, **kwargs ):
        kwargs.setdefault( "size", (1, 1) )
        super(FixHeaderAndFooterLayout, self).__init__(**kwargs)
        self.bind(
                children=self._trigger_layout,
                pos=self._trigger_layout,
                pos_hint=self._trigger_layout,
                size_hint=self._trigger_layout,
                size=self._trigger_layout,  
            )
        
    def do_layout( self, *largs ):
        if self.size == [1, 1]:
            return
        
        layout_width, layout_height = self.size
        layout_left, layout_top = self.pos
        
        header = None
        center = None
        footer = None
        
        if len(self.children) >= 1:
            header = self.children[0]
        if len(self.children) >= 2:
            center = self.children[1]
        if len(self.children) >= 3:
            footer = self.children[2]
        
        if header:
            header.x = layout_left
            header.y = layout_top
            header.width = layout_width
        
        if center:
            y = layout_top
            if header:
                y += header.height

            h = layout_height
            if header:
                h -= header.height
            if footer:
                h -= footer.height
                
            center.x = layout_left
            center.y = y
            center.width = layout_width
            center.height = h
                
        if footer:
            footer.x = layout_left
            footer.y = layout_top + layout_height - footer.height
            footer.width = layout_width
            
    def add_widget(self, widget, index=0):
        widget.bind(
                size=self._trigger_layout,
                size_hint=self._trigger_layout,
                pos=self._trigger_layout,
                pos_hint=self._trigger_layout,
            )
        return super(FixHeaderAndFooterLayout, self).add_widget(widget, index)

    def remove_widget(self, widget):
        widget.unbind(
                size=self._trigger_layout,
                size_hint=self._trigger_layout,
                pos=self._trigger_layout,
                pos_hint=self._trigger_layout,
            )
        return super(FixHeaderAndFooterLayout, self).remove_widget(widget)


class MainWidget(Widget):
    pass

class Layout1App(App):
    pass
    

if __name__ == "__main__":
    Layout1App().run()
