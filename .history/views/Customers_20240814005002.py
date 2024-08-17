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


class Customers(MDScreen):
    def __init__(self, sm, **kwargs):
        super(Customers, self).__init__(**kwargs)

        self.sm = sm

        # Layout to organize the widgets
        layout = BoxLayout(orientation="vertical")

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        try:
            customers = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.customers"
            )

            data_dict = xmltodict.parse(customers.content)
            clients = data_dict["customerss"]["customers"]

            result = [
                (
                    item["city"],
                    item["customerId"],
                    item["dateOfBirth"],
                    item["email"],
                    item["firstName"],
                    item["lastName"],
                    item["phoneNumber"],
                    item["postalAddress"],
                    item["usState"],
                    item["zipCode"],
                )
                for item in clients
            ]

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("City", dp(35)),
                    ("Customer ID", dp(30)),
                    ("Date of Birth", dp(30)),
                    ("Email", dp(35)),
                    ("First Name", dp(30)),
                    ("Last Name", dp(30)),
                    ("Phone Number", dp(30)),
                    ("Postal Address", dp(50)),
                    ("US State", dp(30)),
                    ("ZIP Code", dp(30)),
                ],
                row_data=result,
                rows_num=10,
                sorted_on="Schedule",
                sorted_order="ASC",
                elevation=2,
            )

            # Add the table to the layout
            heading = Label(text="Account Managers", font_size=40)
            self.add_widget(heading)
            layout.add_widget(self.data_tables)
            self.add_widget(layout)  # Add the layout to the screen
        except:
            raise Exception("There are no resources available for Customers")

    def backToLandingPage(self, instance):
        self.sm.current = "landing"


if __name__ == "__main__":
    Customers().run()
