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

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        ## Form to query stock quotes
        self.form_label = Label(text="Enter stock quote. Eg: AMZN")
        layout.add_widget(self.form_label)
        self.form_input = TextInput(multiline=False, size_hint_y=None, height=60)
        layout.add_widget(self.form_input)
        self.submit_btn = Button(font_size=25, text="Search")
        self.submit_btn.bind(on_press=self.handle_submit)
        layout.add_widget(self.submit_btn)
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

            response = requests.get(url, headers=headers, params=querystring)
            print(response.json())

        except:
            raise Exception("The stock quotes are not available at the moment!")


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
