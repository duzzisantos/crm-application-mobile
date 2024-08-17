from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 3

        entities = ["Managers", "Campaigns", "Customers", "Enrollments", "Products"]

        for item in entities:
            self[item] = Button(text=item, font_size=40)
            self.add_widget(self[item])


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
