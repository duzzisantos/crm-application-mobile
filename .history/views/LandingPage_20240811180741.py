from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Good Day Admin"))


class Main(App):
    def build(self):
        return LandingPage()


Main().run()
