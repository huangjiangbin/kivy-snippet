# encoding: utf-8
import kivy
from kivy.app import App
from kivy.uix.image import Image
import pygame

class MyApp(App):
    def build(self):
        return Image(source="a.jpg", pos=(0, 0), size=(650, 260))

if __name__ == '__main__':
    MyApp().run()
