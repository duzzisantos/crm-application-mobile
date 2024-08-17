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


class Campaigns(MDScreen):
    def __init__(self, sm, **kwargs):
        super(Campaigns, self).__init__(**kwargs)

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
            le_campaign = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.campaigns"
            )

            data_dict = xmltodict.parse(le_campaign.content)
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

            # Add the table to the layout
            heading = Label(text="Account Managers", font_size=40)
            self.add_widget(heading)
            layout.add_widget(self.data_tables)
            self.add_widget(layout)  # Add the layout to the screen

        except:
            raise Exception("There are no resources available for Campaigns")

    def backToLandingPage(self, instance):
        self.sm.current = "landing"


if __name__ == "__main__":
    Campaigns().run()
