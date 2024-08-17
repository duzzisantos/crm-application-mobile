from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable


class AccountManagers(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                "Account Manager ID",
                "First Name",
                "Last Name",
                "Product Specialization",
                "Date of Employment",
                "Grade Level",
                "Email",
                "Phone",
            ],
        )


if __name__ == "__main__":
    AccountManagers().run()
