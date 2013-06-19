# encoding: utf-8
import kivy
from kivy.app import App
from kivy.uix.label import Label
import urllib2
import re

class MyApp(App):
    def build(self):
        try:
            url = "http://www.baidu.com"
            text = urllib2.urlopen( url ).read()
            text = re.findall("<title>(.*)</title>", text)[0]
            text = text.decode("utf-8")
        except Exception, e:
            text = "url get failed %s"%(str(e))
            
        print text
        
        a = Label()
        a.text = text
        a.font_name = "msyh.ttf"
        return a

if __name__ == '__main__':
    MyApp().run()
