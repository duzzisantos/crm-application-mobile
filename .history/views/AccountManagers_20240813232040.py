from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen, Screen

import requests
import json
import xmltodict


class AccountManagers(Screen):
    def build(self):

        goBack = Button(text="< Back")

        try:
            accountManagerList = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.accountmanagers"
            )

            data_dict = xmltodict.parse(accountManagerList.content)
            account_managers = data_dict["accountmanagerss"]["accountmanagers"]

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
                rows_num=10,
                sorted_on="Schedule",
                sorted_order="ASC",
                elevation=2,
            )

            screen = MDScreen()
            screen.add_widget(self.data_tables)
            return screen
        except:
            raise Exception("There are no resources available for Account Managers")


if __name__ == "__main__":
    AccountManagers().run()
