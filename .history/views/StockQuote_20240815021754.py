from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout

import requests


class StockQuotes(MDScreen):
    def __init__(self, sm, **kwargs):
        super(StockQuotes, self).__init__(**kwargs)
        self.sm = sm
        self.form_text = ""

        # Layout to organize the widgets
        layout = BoxLayout(orientation="vertical")
        innerLayout = BoxLayout(orientation="horizontal", padding=[60, 80])

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        header = Label(
            text="Stock Quotes (Powered by Yahoo Finance)",
            font_size=40,
            color="#000000",
            size_hint=[0.9, 0.2],
            padding=[40, 40],
            bold=True,
        )
        layout.add_widget(header)

        ## Form to query stock quotes

        self.form_input = TextInput(
            multiline=False,
            size_hint_y=None,
            size_hint_x=None,
            height=100,
            width=450,
            hint_text="Enter stock name. Eg: MSFT",
            is_focusable=True,
            padding=[15, 15],
            center=[0.5, 0.5],
        )
        innerLayout.add_widget(self.form_input)

        self.submit_btn = Button(
            font_size=35,
            text="Search Stock",
            height=103,
            width=300,
            size_hint_y=None,
            size_hint_x=None,
            background_color="#222a68",
        )
        self.submit_btn.bind(on_press=self.handle_submit)
        innerLayout.add_widget(self.submit_btn)

        layout.add_widget(innerLayout)

        place_holder = Label(text="")
        layout.add_widget(place_holder)
        self.add_widget(layout)

        ## To previous page - event handler

    def backToLandingPage(self, instance):
        self.sm.current = "landing"

    ## grab input search data to be added to query parameters
    def handle_submit(self, instance):
        self.form_text = self.form_input.text

        ## Fetch stock quote data and handle error gracefully
        try:

            url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"

            querystring = {"ticker": str(self.form_text), "module": "statistics"}

            headers = {
                "x-rapidapi-key": "1f6aba5149msha00241a4cbf041fp12ab4ajsn0544aef4b5de",
                "x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
            }

            result = requests.get(url, headers=headers, params=querystring)
            response = result.json()

            ## Stock results quoted in table: table row and column items
            symbol = response["meta"]["symbol"]
            last_updated = response["meta"]["processedTime"]
            ent_value = response["body"]["enterpriseValue"]["fmt"]
            forward_pe = response["body"]["forwardPE"]["fmt"]
            profit_margins = response["body"]["profitMargins"]["fmt"]
            float_shares = response["body"]["floatShares"]["fmt"]
            fifty_two_week_change = response["body"]["52WeekChange"]["fmt"]
            shares_outstanding = response["body"]["sharesOutstanding"]["fmt"]

            stock_column_headers = [
                ("Stock symbol", dp(30)),
                ("Last updated", dp(45)),
                ("Enterprise value", dp(30)),
                ("Forward P/E", dp(30)),
                ("Profit margins", dp(30)),
                ("Float shares", dp(30)),
                ("52-week change", dp(30)),
                ("Shares outstanding", dp(30)),
            ]

            stock_row_data = [
                (
                    symbol,
                    last_updated,
                    ent_value,
                    forward_pe,
                    profit_margins,
                    float_shares,
                    fifty_two_week_change,
                    shares_outstanding,
                )
            ]

            self.stock_table = MDDataTable(
                row_data=stock_row_data,
                column_data=stock_column_headers,
                elevation=2,
                size_hint=[1, 0.5],
                height=dp(15),
            )

            place_label = Label(text="")
            self.add_widget(self.stock_table)
            self.add_widget(place_label)

        except:
            print("The stock quotes are not available at the moment!")
            error_message = Label(
                text="Error in processing request, Please check stock ticker and try again!",
                color="red",
                padding=[25, 25],
            )
            self.add_widget(error_message)


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        # Create the AccountManagers screen and pass ScreenManager to it
        stock_quotes_screen = StockQuotes(sm, name="stock_quotes")
        sm.add_widget(stock_quotes_screen)

        # Add the landing page screen (You need to define this similarly)
        landing_screen = MDScreen(name="landing")
        sm.add_widget(landing_screen)

        sm.current = "landing"  # Start with the landing page
        return sm


if __name__ == "__main__":
    MyApp().run()
