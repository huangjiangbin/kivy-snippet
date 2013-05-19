# encoding: utf-8
#
# msyh.ttf是字体文件
# 随便找一个中文字体，复制到hello_world_in_chinese.py同目录下
# 把msyh.ttf改成相应的文件名即可
#
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        a = Label()
        a.font_name = "msyh.ttf"
        a.text = u"你好，世界！"
        return a

if __name__ == "__main__":
    MyApp().run()
