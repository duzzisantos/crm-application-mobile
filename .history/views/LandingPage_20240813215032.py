from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import AccountManagers, Campaigns, Customers, Enrollments, Product


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")

        managerBtn = Button(text="Account Managers")
        layout.add_widget(managerBtn)


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
