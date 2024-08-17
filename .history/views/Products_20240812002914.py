from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
import requests
import json
import xmltodict


class Products(MDApp):
    def build(self):

        try:
            products = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.products"
            )

            data_dict = xmltodict.parse(products.content)
            account_managers = data_dict["productss"]["products"]

            result = [
                (
                    manager["accountManagerId"],
                    manager["dateOfEmployment"],
                    manager["email"],
                    manager["firstName"],
                    manager["gradeLevel"],
                    manager["lastName"],
                    manager["phoneNumber"],
                    manager["productSpecialization"],
                )
                for manager in account_managers
            ]

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Account Manager ID", dp(45)),
                    ("Date of Employment", dp(40)),
                    ("Email", dp(40)),
                    ("First Name", dp(40)),
                    ("Grade Level", dp(30)),
                    ("Last Name", dp(30)),
                    ("Phone", dp(30)),
                    ("Product Specialization", dp(45)),
                ],
                row_data=result,
                sorted_on="Schedule",
                sorted_order="ASC",
                elevation=2,
            )

            screen = MDScreen()
            screen.add_widget(self.data_tables)
            return screen
        except:
            raise Exception("There are no resources available for Products")


if __name__ == "__main__":
    Products().run()
