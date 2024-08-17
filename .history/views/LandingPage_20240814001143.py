from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import AccountManagers
import Campaigns
import Customers
import Product
import Enrollments


from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, sm, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 5
        self.sm = sm

        self.orientation = "lr-tb"

        ## Button widgets for navigating through screens

        ##Account managers
        self.managerBtn = Button(text="Account Managers", font_size=40)
        self.managerBtn.bind(on_press=self.showManagers)
        self.add_widget(self.managerBtn)

        ##Campaigns
        self.campaignBtn = Button(text="Campaigns", font_size=40)
        self.campaignBtn.bind(on_press=self.showCampaigns)
        self.add_widget(self.campaignBtn)

        # Customers
        self.customersBtn = Button(text="Customers", font_size=40)
        self.customersBtn.bind(on_press=self.showCustomers)
        self.add_widget(self.customersBtn)

        ##Enrollments
        self.enrollmentBtn = Button(text="Enrollments", font_size=40)
        self.enrollmentBtn.bind(on_press=self.showEnrollments)
        self.add_widget(self.enrollmentBtn)

        ##Products
        self.productsBtn = Button(text="Products", font_size=40)
        self.productsBtn.bind(on_press=self.showProducts)
        self.add_widget(self.productsBtn)

        ##Stock quotes
        self.yahooFinance = Button(text="Yahoo Finance", font_size=40)

        self.add_widget(self.yahooFinance)

    ## Click event handlers
    def showManagers(self, instance):
        self.sm.current = "account_managers"

    def showCampaigns(self, instance):
        self.sm.current = "show_campaigns"

    def showCustomers(self, instance):
        self.sm.current = "customers"

    def showEnrollments(self, instance):
        self.sm.current = "enrollments"

    def showProducts(self, instance):
        self.sm.current = "products"

    def showStockQuotes(self, instance):
        self.sm.current = "yahoo_finance"


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(AccountManagers.AccountManagers(sm=sm, name="account_managers"))
        # sm.add_widget(Campaigns.Campaigns(name="campaigns"))
        sm.add_widget(Campaigns.Campaigns(sm=sm, name="show_campaigns"))
        sm.add_widget(Product.Products(name="products"))
        sm.add_widget(Customers.Customers(name="customers"))
        sm.add_widget(Enrollments.Enrollments(name="enrollments"))

        landing_page = LandingPage(sm)
        landing_screen = Screen(name="landing")
        landing_screen.add_widget(landing_page)
        sm.add_widget(landing_screen)

        sm.current = "landing"
        return sm


if __name__ == "__main__":
    MyApp().run()
