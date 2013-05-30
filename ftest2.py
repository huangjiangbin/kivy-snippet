# encoding: utf-8
"""
通过代码，查找到系统中的支持中文的字体文件，然后给font_name赋值即可
所有需要一个辅助函数来做这件事情
而且还需要了解各个操作系统的字体文件的保存位置
各操作系统会自带那些字体能支持中文
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
import pygame

class MyApp(App):
    def build(self):
        a = Label()
        a.text = u"这里是中文哦"
        a.font_name = "/usr/share/cups/fonts/FreeMono.ttf"
        return a

if __name__ == '__main__':
    MyApp().run()
