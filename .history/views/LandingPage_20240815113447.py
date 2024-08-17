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
import StockQuote


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
        self.managerBtn = Button(
            text="Account Managers 🧑🏽",
            font_size=40,
            color="white",
            background_color="cyan",
            bold=True,
        )
        self.managerBtn.bind(on_press=self.showManagers)
        self.add_widget(self.managerBtn)

        ##Campaigns
        self.campaignBtn = Button(
            text="Campaigns",
            font_size=40,
            background_color="#6ca6c1",
            bold=True,
        )
        self.campaignBtn.bind(on_press=self.showCampaigns)
        self.add_widget(self.campaignBtn)

        # Customers
        self.customersBtn = Button(
            text="Customers",
            font_size=40,
            background_color="#2f3061",
            color="white",
            bold=True,
        )
        self.customersBtn.bind(on_press=self.showCustomers)
        self.add_widget(self.customersBtn)

        ##Enrollments
        self.enrollmentBtn = Button(
            text="Enrollments",
            font_size=40,
            background_color="#06aed5",
            bold=True,
        )
        self.enrollmentBtn.bind(on_press=self.showEnrollments)
        self.add_widget(self.enrollmentBtn)

        ##Products
        self.productsBtn = Button(
            text="Products",
            font_size=40,
            background_color="#004e89",
            bold=True,
        )
        self.productsBtn.bind(on_press=self.showProducts)
        self.add_widget(self.productsBtn)

        ##Stock quotes
        self.stockQuotesBtn = Button(
            text="Stock Quotes",
            font_size=40,
            background_color="#222a68",
            bold=True,
        )
        self.stockQuotesBtn.bind(on_press=self.showStockQuotes)
        self.add_widget(self.stockQuotesBtn)

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
        self.sm.current = "stock_quotes"


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        ## All displayable screens rendered by screen manager
        sm.add_widget(AccountManagers.AccountManagers(sm=sm, name="account_managers"))
        sm.add_widget(Campaigns.Campaigns(sm=sm, name="show_campaigns"))
        sm.add_widget(Product.Products(sm=sm, name="products"))
        sm.add_widget(Customers.Customers(sm=sm, name="customers"))
        sm.add_widget(Enrollments.Enrollments(sm=sm, name="enrollments"))
        sm.add_widget(StockQuote.StockQuotes(sm=sm, name="stock_quotes"))

        landing_page = LandingPage(sm)
        landing_screen = Screen(name="landing")
        landing_screen.add_widget(landing_page)
        sm.add_widget(landing_screen)

        sm.current = "landing"
        return sm


if __name__ == "__main__":
    MyApp().run()
