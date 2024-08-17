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


class Products(MDScreen):
    def __init__(self, sm, **kwargs):
        super(Products, self).__init__(**kwargs)

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

            # Add the table to the layout
            heading = Label(text="Products", font_size=40)
            self.add_widget(heading)
            layout.add_widget(self.data_tables)
            self.add_widget(layout)  # Add the layout to the screen
        except:
            raise Exception("There are no resources available for Products")

    # Go back event handler
    def backToLandingPage(self, instance):
        self.sm.current = "landing"


if __name__ == "__main__":
    Products().run()
