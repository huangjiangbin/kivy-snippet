# coding: utf-8
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.utils import platform
import pygame
import os
import sys

__platform = platform()
if __platform == 'android':
    if os.path.exists( "/system/fonts/DroidSansFallback.ttf" ):
        Label.font_name = StringProperty( "/system/fonts/DroidSansFallback.ttf" )
elif __platform == 'win':
    st = pygame.font.match_font("stsong")
    if os.path.exists( st ):
        Label.font_name = StringProperty( st )

class ViewLogin( Widget ):
    pass

class IpwApp( App ):
    def build( self ):
        return ViewLogin( )

if __name__ == '__main__':
    IpwApp().run()
