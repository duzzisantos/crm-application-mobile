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
                "http://localhost:8080/CRMApplication/webresources/entity.campaignenrollments"
            )

            data_dict = xmltodict.parse(products.content)
            enrollments = data_dict["campaignsenrollmentss"]["campaignenrollments"]

            result = [
                (
                    item["accountManagerId"],
                    item["campaignContent"],
                    item["campaignId"],
                    item["campaignManager"],
                    item["campaignName"],
                    item["customerId"],
                    item["enrollmentId"],
                    item["hasResponded"],
                    item["offeredPrice"],
                    item["productId"],
                    item["purchaseQuantity"],
                )
                for item in enrollments
            ]

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Account Manager ID", dp(45)),
                    ("Campaign Content", dp(45)),
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
            raise Exception("There are no resources available for Enrollments")


if __name__ == "__main__":
    Products().run()
