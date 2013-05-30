# encoding: utf-8
import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.loader import Loader
import pygame

class MyApp(App):
    def build(self):
        return AsyncImage(
            source="http://css.emai.com/public/images/logo.gif",
            pos=(0,0),
            size=(160,56),
            )
        

if __name__ == '__main__':
    MyApp().run()
