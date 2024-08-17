from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import requests
import xmltodict


class AccountManagers(MDScreen):
    def __init__(self, sm, **kwargs):
        super(AccountManagers, self).__init__(**kwargs)
        self.sm = sm  # Reference to ScreenManager for navigation

        # Layout to organize the widgets
        layout = BoxLayout(orientation="vertical")

        # Back button
        goBack = Button(
            text="<< Back", font_size=25, size_hint=(None, None), size=(dp(100), dp(40))
        )
        goBack.bind(on_press=self.backToLandingPage)
        layout.add_widget(goBack)

        header = Label(
            text="Account Managers",
            font_size=40,
            color="#000000",
            size_hint=[0.9, 0.1],
            padding=[40, 40],
            bold=True,
        )
        layout.add_widget(header)

        try:
            # Fetch account manager data
            accountManagerList = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.accountmanagers"
            )

            # Parse the XML data
            data_dict = xmltodict.parse(accountManagerList.content)
            account_managers = data_dict["accountmanagerss"]["accountmanagers"]

            # Prepare the data for the table
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
                    MDRaisedButton(
                        text="Delete",
                        size_hint=[None, None],
                        size=(dp(80), dp(30)),
                        on_release=lambda x, id=manager[
                            "accountManagerId"
                        ]: self.delete_manager(id),
                    ),
                )
                for manager in account_managers
            ]

            # Create the data table
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
                    ("Action", dp(30)),
                ],
                row_data=result,
                rows_num=10,
                sorted_on="Schedule",
                sorted_order="ASC",
                elevation=2,
            )

            # Add the table to the layout

            layout.add_widget(self.data_tables)
            self.add_widget(layout)  # Add the layout to the screen
        except:
            raise Exception("There are no resources available for Account Managers")

    def backToLandingPage(self, instance):
        self.sm.current = "landing"

    def delete_manager(self, id):
        print("Deleted: " + id)


class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()

        # Create the AccountManagers screen and pass ScreenManager to it
        account_managers_screen = AccountManagers(sm, name="account_managers")
        sm.add_widget(account_managers_screen)

        # Add the landing page screen (You need to define this similarly)
        landing_screen = MDScreen(name="landing")
        sm.add_widget(landing_screen)

        sm.current = "landing"  # Start with the landing page
        return sm


if __name__ == "__main__":
    MyApp().run()
