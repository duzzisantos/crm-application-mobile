from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion
from kivy.uix.gridlayout import GridLayout


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.height = 90
        self.add_widget(Label(text="Good Day Admin, Welcome to Funnel CRM"))

        # Dynamically add accordion for each entity we want to display, so that on expand, we can find the associated table
        self.entities = [
            "Account Managers",
            "Campaigns",
            "Customers",
            "Enrollments",
            "Products",
        ]

        for item in self.entities:
            self.add_widget(Accordion(text=item))
            return item


class Main(App):
    def build(self):
        return LandingPage()


Main().run()
