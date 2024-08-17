from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")

        self.managerBtn = Button(text="Account Managers")
        self.layout.add_widget(managerBtn)


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
