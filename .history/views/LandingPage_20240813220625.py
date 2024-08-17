from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 3

        entities = ["managers", "campaigns", "customers", "enrollments", "products"]

        for item in entities:
            self[item] = Button(text=item.capitalize(), font=40)


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
