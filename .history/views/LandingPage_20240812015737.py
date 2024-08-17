from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_file("kv_templates/tabs.kv")


class LandingPage(TabbedPanel):
    pass


class Main(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    Main().run()
