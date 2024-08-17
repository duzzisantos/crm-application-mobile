from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import AccountManagers
import Campaigns

from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, sm, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 5
        self.sm = sm

        self.orientation = "lr-tb"

        ## Button widgets for navigating through screens
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
        self.sm.current = "account_managers"

    def showCampaigns(self, instance):
        self.sm.current = "campaigns"

    def showCustoemrs(self, instance):
        self.sm.current = "customers"

    def showEnrollments(self, instance):
        self.sm.current = "enrollments"

    def showProducts(self, instance):
        self.sm.current = "products"


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(AccountManagers(name="account_managers"))
        sm.add_widget(Campaigns(name="campaigns"))

        landing_page = LandingPage(sm)
        landing_screen = Screen(name="landing")
        landing_screen.add_widget(landing_page)
        sm.add_widget(landing_screen)

        sm.current = "landing"
        return sm


if __name__ == "__main__":
    MyApp().run()
