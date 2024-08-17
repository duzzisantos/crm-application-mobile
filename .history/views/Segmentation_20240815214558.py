from kivymd.app import MDApp
from kivy.uix.recycleview import RecycleView
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import requests
import xmltodict


class Segmentation(MDScreen):
    def __init__(self, sm, **kwargs):
        super(Segmentation, self).__init__(**kwargs)

        self.sm = sm

        ## Regions in the US with which to create market segmentation
        us_regions = [
            {
                "region": "Northeast",
                "states": [
                    "Connecticut",
                    "Maine",
                    "Massachusetts",
                    "New Hampshire",
                    "Rhode Island",
                    "Vermont",
                    "New Jersey",
                    "New York",
                    "Pennsylvania",
                ],
            },
            {
                "region": "South",
                "states": [
                    "Delaware",
                    "Florida",
                    "Georgia",
                    "Maryland",
                    "North Carolina",
                    "South Carolina",
                    "Virginia",
                    "West Virginia",
                    "Alabama",
                    "Kentucky",
                    "Mississippi",
                    "Tennessee",
                    "Arkansas",
                    "Louisiana",
                    "Oklahoma",
                    "Texas",
                ],
            },
            {
                "region": "Midwest",
                "states": [
                    "Illinois",
                    "Indiana",
                    "Michigan",
                    "Ohio",
                    "Wisconsin",
                    "Iowa",
                    "Kansas",
                    "Minnesota",
                    "Missouri",
                    "Nebraska",
                    "North Dakota",
                    "South Dakota",
                ],
            },
            {
                "region": "West",
                "states": [
                    "Arizona",
                    "Colorado",
                    "Idaho",
                    "Montana",
                    "Nevada",
                    "New Mexico",
                    "Utah",
                    "Wyoming",
                    "Alaska",
                    "California",
                    "Hawaii",
                    "Oregon",
                    "Washington",
                ],
            },
        ]

        layout = BoxLayout(orientation="vertical")

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        header = Label(
            text="Market Segmentation",
            font_size=40,
            color="#000000",
            size_hint=[0.9, 0.1],
            padding=[40, 40],
            bold=True,
        )
        layout.add_widget(header)

        try:
            customers = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.customers"
            )

            ##Convert API response from XML to JSON dictionary
            data_dict = xmltodict.parse(customers.content)
            clients = data_dict["customerss"]["customers"]

            segmentation_by_region = []
            for customer in clients:
                for region in us_regions:
                    for state in region["states"]:
                        if customer["usState"].__eq__(state):
                            segmentation_by_region.append(
                                {
                                    "covered_region": region["region"],
                                    "state": state,
                                    "total_client_size": region["states"].count(state),
                                }
                            )

            print(segmentation_by_region)

        except:
            raise Exception("There are no resources available for Customers")

    def backToLandingPage(self, instance):
        self.sm.current = "landing"


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        Window.title = "Market Segmentation"

        # Create the Segmentation screen and pass ScreenManager to it
        segments_screen = Segmentation(sm, name="segmentation")
        sm.add_widget(segments_screen)

        # Add the landing page screen (You need to define this similarly)
        landing_screen = MDScreen(name="landing")
        sm.add_widget(landing_screen)

        sm.current = "landing"  # Start with the landing page
        return sm


if __name__ == "__main__":
    Segmentation().run()
