from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import requests
import xmltodict


class StockQuotes(MDScreen):
    def __init__(self, sm, **kwargs):
        super(StockQuotes, self).__init__(**kwargs)
        self.sm = sm

        # Layout to organize the widgets
        layout = BoxLayout(orientation="vertical")

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        ## Fetch stock quote data and handle error gracefully
        try:

            stockQuoteData = requests.get()

        except:
            raise Exception("The stock quotes are not available at the moment!")
