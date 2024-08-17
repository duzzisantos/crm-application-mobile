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
            articles = data_dict["productss"]["products"]

            result = [
                (
                    item["productCategory"],
                    item["productId"],
                    item["productManager"],
                    item["productManufacturer"],
                    item["productName"],
                    item["productOrigin"],
                    item["productPrice"],
                )
                for item in articles
            ]

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Product Category", dp(40)),
                    ("Product ID", dp(65)),
                    ("Product Manager", dp(35)),
                    ("Manufacturer", dp(30)),
                    ("Product Name", dp(30)),
                    ("Origin", dp(30)),
                    ("Price", dp(30)),
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
            raise Exception("There are no resources available for Products")


if __name__ == "__main__":
    Products().run()
