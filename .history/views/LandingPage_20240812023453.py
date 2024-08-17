from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivymd.app import MDApp
import AccountManagers, Campaigns, Customers, Enrollments, Products


class LandingPage(TabbedPanel):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.do_default_tab = False
        self.tab_pos = "top_left"

        self.add_widget(
            TabbedPanelItem(text="Managers List", content=AccountManagers(MDApp))
        )
        self.add_widget(
            TabbedPanelItem(text="Campaigns List", content=Campaigns(MDApp))
        )
        self.add_widget(TabbedPanelItem(text="Customers", content=Customers(MDApp)))
        self.add_widget(
            TabbedPanelItem(text="Enrollments List", content=Enrollments(MDApp))
        )
        self.add_widget(TabbedPanelItem(text="Product List", content=Products(MDApp)))


class Products(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
