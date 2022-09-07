# from kivy.config import Config
# Config.set('graphics', 'width', '350')
# Config.set('graphics', 'height', '650')
import json
import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

Builder.load_file('screens/login.kv')


class Login(ScrollView):
    def __init__(self, **kwargs): 
        super(Login, self).__init__(**kwargs)
        Window.softinput_mode = "below_target"
    
    def login(self,):
        api = "http://192.168.0.11:8000/login"
        if self.ids["usuario"].text == "" or self.ids["senha"].text == "":
            box = BoxLayout(orientation="vertical")
            msg = Label(text="Email/senha vazios!")
            box.add_widget(msg)
            pop = Popup(title="", content=box, size_hint=(None, None), separator_height=0, background="",
            size=(300, 60), pos_hint={"top": 0.97}, background_color=(220/255, 53/255, 69/255, 1))
            pop.open()
            return

        data = {
            "email" : self.ids["usuario"].text,
            "senha" : self.ids["senha"].text
        }

        # response = requests.post(url=api, data=data)
        # response = json.loads(response.content.decode())
        # box = BoxLayout(orientation="vertical")
        # msg = Label(text=response["msg"])
        # box.add_widget(msg)
        # pop = Popup(title="", content=box, size_hint=(None, None), separator_height=0, background="",
        #     size=(300, 60), pos_hint={"top": 0.97}, background_color=response["color_msg"])
        # pop.open()
    
class ExekeApp(App):
    def build(self):
        # Window.size = (720, 1440)
        return Login()
    
if __name__ == '__main__':
    ExekeApp().run()