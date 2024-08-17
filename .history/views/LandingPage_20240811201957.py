from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.datatables import MDDataTable
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_file("kv_templates/tabs.kv")


class LandingPage(TabbedPanel):
    pass
    # # Dynamically add accordion for each entity we want to display, so that on expand, we can find the associated table
    # entities = [
    #     "Account Managers",
    #     "Campaigns",
    #     "Customers",
    #     "Enrollments",
    #     "Products",
    # ]


class Main(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    Main().run()
