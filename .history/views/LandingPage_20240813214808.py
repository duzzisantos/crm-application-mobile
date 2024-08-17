from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import AccountManagers, Campaigns, Customers, Enrollments, Product


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")

        entities = [
            "Account Managers",
            "Campaigns",
            "Customers",
            "Enrollments",
            "Prodducts",
        ]
        i = 0
        while i < len(entities):
            i += 1
            for element in entities:
                button = Button(text=element)
                layout.add_widget(button[i])
            return element


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
