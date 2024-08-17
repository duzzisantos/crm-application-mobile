from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)

        # Dynamically add accordion for each entity we want to display, so that on expand, we can find the associated table
        entities = [
            "Account Managers",
            "Campaigns",
            "Customers",
            "Enrollments",
            "Products",
        ]

        outerElement = BoxLayout(height=90)
        rootElement = Accordion()
        for item in entities:
            element = AccordionItem(
                title=item,
                orientation="vertical",
                min_space=60,
                background_normal="image_when_collapsed.png",
                background_selected="image_when_selected.png",
            )
            element.add_widget(Label(text=item))
            rootElement.add_widget(element)

        outerElement.add_widget(rootElement)

        self.add_widget(outerElement)


class Main(App):
    def build(self):
        return LandingPage()


Main().run()
