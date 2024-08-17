from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
import requests
import json
import xmltodict


class AccountManagers(MDApp):
    def build(self):

        try:
            accountManagerList = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.accountmanagers"
            )

            data_dict = xmltodict.parse(accountManagerList.content)
            json_data = json.dumps(data_dict, indent=4)
            print(json_data)

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Account Manager ID", dp(30)),
                    ("Date of Employment", dp(30)),
                    ("Email", dp(30)),
                    ("First Name", dp(30)),
                    ("Grade Level", dp(30)),
                    ("Last Name", dp(30)),
                    ("Phone", dp(30)),
                    ("Product Specialization", dp(30)),
                ],
                row_data=json_data,
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
