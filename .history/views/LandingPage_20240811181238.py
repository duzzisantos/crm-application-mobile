from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Good Day Admin, Welcome to Funnel CRM"))


class Main(App):
    def build(self):
        return LandingPage()


Main().run()
