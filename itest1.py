# encoding: utf-8
#
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        self.update_canvas()
        
    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            self.windrose = Ellipse(source="500px-Windrose.svg.png", pos=self.pos, size=self.size)

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()
