from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import AccountManagers
import Campaigns

from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 5

        self.orientation = "lr-tb"

        self.managerBtn = Button(text="Account Managers", font_size=40)
        self.add_widget(self.managerBtn)
        self.campaignBtn = Button(text="Campaigns", font_size=40)
        self.add_widget(self.campaignBtn)
        self.customersBtn = Button(text="Customers", font_size=40)
        self.add_widget(self.customersBtn)
        self.enrollmentBtn = Button(text="Enrollments", font_size=40)
        self.add_widget(self.enrollmentBtn)
        self.productsBtn = Button(text="Products", font_size=40)
        self.add_widget(self.productsBtn)
        self.yahooFinance = Button(text="Yahoo Finance", font_size=40)
        self.yahooFinance.bind(on_press=self.showManagers)
        self.add_widget(self.yahooFinance)

    ## Click event handlers

    def showManagers(self, instance):
        sm = ScreenManager()

        sm.add_widget(AccountManagers)

        print("Pressed show managers")


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
