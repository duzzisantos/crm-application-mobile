from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion
from kivy.uix.boxlayout import BoxLayout


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.height = 90
        self.add_widget(Label(text="Good Day Admin, Welcome to Funnel CRM"))

        entities = [
            "Account Managers",
            "Campaigns",
            "Customers",
            "Enrollments",
            "Products",
        ]
        for element in entities:
            self.add_widget(Accordion(text=element))


class Main(App):
    def build(self):
        return LandingPage()


Main().run()
