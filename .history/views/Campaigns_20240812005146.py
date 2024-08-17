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
                "http://localhost:8080/CRMApplication/webresources/entity.campaigns"
            )

            data_dict = xmltodict.parse(products.content)
            campaigns = data_dict["campaignss"]["campaigns"]

            result = [
                (
                    item["accountManagerId"],
                    item["campaignEnd"],
                    item["campaignId"],
                    item["campaignManager"],
                    item["campaignName"],
                    item["campaignProduct"],
                    item["campaignSalesValueTarget"],
                    item["campaignSalesVolumeTarget"],
                    item["campaignStart"],
                    item["campaignType"],
                    item["productId"],
                )
                for item in campaigns
            ]

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Account Manager ID", dp(45)),
                    ("Campaign End", dp(45)),
                    ("Campaign ID", dp(30)),
                    ("Campaign Manager", dp(35)),
                    ("Campaign Name", dp(30)),
                    ("Product", dp(30)),
                    ("Sales Value Target", dp(35)),
                    ("Sales Volume Target", dp(35)),
                    ("Campaign Start", dp(45)),
                    ("Type", dp(25)),
                    ("Product ID", dp(30)),
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
