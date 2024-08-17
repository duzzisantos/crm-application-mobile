from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
import requests
import json
import xmltodict


class Customers(MDApp):
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
                    ("Account Manager ID", dp(45)),
                    ("Campaign Content", dp(65)),
                    ("Campaign ID", dp(30)),
                    ("Campaign Manager", dp(35)),
                    ("Campaign Name", dp(30)),
                    ("Customer ID", dp(30)),
                    ("Enrollment ID", dp(30)),
                    ("Has Responded", dp(30)),
                    ("Offered Price", dp(30)),
                    ("Product ID", dp(30)),
                    ("Purchase Quantity", dp(30)),
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
