import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import *
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics', 'resizable', '1') 
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class LoginPage(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def check(self):
        if self.username.text == "Tom" and self.password.text == "password1":
            print("YES")

    def reset(self):
        self.username.text = ""
        self.password.text = ""

class MainPage(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginPage(name="login"))
sm.add_widget(MainPage(name="main"))

class Application(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginPage(name="login"))
        sm.add_widget(MainPage(name="main"))
        return sm

if __name__ == "__main__":
    Application().run()