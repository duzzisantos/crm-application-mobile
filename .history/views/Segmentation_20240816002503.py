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
            text="Market Segmentation by Region and State",
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

            ## Extrapolate regional statistics from clients API result (data from database)
            ## through mapping the state and regional data with established regional categorization dataset
            ## With this, we can segment customers based on state and region, and population size
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

            ## Render market segmentation by region only: an aggregate of customer size across all states
            ## presented as top-level regional overview: Example: Midwest - 450, South - 490 etc.
            regional_overview = {}
            for each in segmentation_by_region:
                selected_region = each["covered_region"]
                selected_state = each["state"]
                selected_customer_size = each["total_client_size"]

                if selected_region not in regional_overview:
                    regional_overview[selected_region] = {
                        "state": set(),
                        "total_customer_size": 0,
                    }

                ## increment state count and add aggregate customer size per region
                regional_overview[selected_region]["state"].add(selected_state)
                regional_overview[selected_region][
                    "total_customer_size"
                ] += selected_customer_size

            aggregate_table_row_data = [
                (region, len(values["state"]), values["total_customer_size"])
                for region, values in regional_overview.items()
            ]

            ## Create aggregate segmentation table
            self.aggregate_table = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Region", dp(35)),
                    ("Total States", dp(30)),
                    ("Total Customer Size", dp(45)),
                ],
                row_data=aggregate_table_row_data,
                sorted_on="Schedule",
                sorted_order="ASC",
                elevation=2,
            )

            ## Display tables on layout and

            layout.add_widget(self.aggregate_table)
            self.add_widget(layout)

        except:
            raise Exception(
                "Either there are no resources available for Customers or the server is not running yet"
            )

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
