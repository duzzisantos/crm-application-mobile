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


class Enrollments(MDScreen):
    def __init__(self, sm, **kwargs):
        super(Enrollments, self).__init__(**kwargs)

        self.sm = sm

        # Layout to organize the widgets
        layout = BoxLayout(orientation="vertical")

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        header = Label(
            text="Enrollments",
            font_size=30,
            color="#000000",
            size_hint=[0.9, 0.1],
            padding=[40, 40],
        )
        layout.add_widget(header)

        try:
            products = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.campaignenrollments"
            )

            data_dict = xmltodict.parse(products.content)
            enrollments = data_dict["campaignenrollmentss"]["campaignenrollments"]

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

            # Add the table to the layout
            heading = Label(text="Enrollments", font_size=40)
            self.add_widget(heading)
            layout.add_widget(self.data_tables)
            self.add_widget(layout)  # Add the layout to the screen
        except:
            raise Exception("There are no resources available for Enrollments")

    def backToLandingPage(self, instance):
        self.sm.current = "landing"


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        # Create the AccountManagers screen and pass ScreenManager to it
        enrollment_screen = Enrollments(sm, name="enrollments")
        sm.add_widget(enrollment_screen)

        # Add the landing page screen (You need to define this similarly)
        landing_screen = MDScreen(name="landing")
        sm.add_widget(landing_screen)

        sm.current = "landing"  # Start with the landing page
        return sm


if __name__ == "__main__":
    Enrollments().run()
