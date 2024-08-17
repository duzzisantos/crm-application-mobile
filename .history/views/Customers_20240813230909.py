from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen, Screen
import requests
import json
import xmltodict


class Customers(Screen):
    def build(self):

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

            screen = MDScreen()
            screen.add_widget(self.data_tables)
            return screen
        except:
            raise Exception("There are no resources available for Customers")


if __name__ == "__main__":
    Customers().run()
