from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import requests


class AccountManagers(MDApp):
    def build(self):

        self.accountManagerList = []

        try:
            self.accountManagerList = requests.get(
                "http://localhost:8080/CRMApplication/webresources/entity.accountmanagers"
            )

            self.data_tables = MDDataTable(
                use_pagination=True,
                check=True,
                column_data=[
                    ("Account Manager ID", dp(30)),
                    ("First Name", dp(30)),
                    ("Last Name", dp(30)),
                    ("Product Specialization", dp(30)),
                    ("Date of Employment", dp(30), self.sort_on_doe),
                    ("Grade Level", dp(30), self.sort_on_grade_level),
                    ("Email", dp(30)),
                    ("Phone", dp(30)),
                ],
                row_data=self.accountManagerList.json(),
            )
        except:
            raise Exception("There are no resources available for Account Managers")


if __name__ == "__main__":
    AccountManagers().run()
