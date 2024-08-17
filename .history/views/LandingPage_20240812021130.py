from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class LandingPage(TabbedPanel):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.do_default_tab = False
        self.tab_pos = "top_left"

        self.add_widget(
            TabbedPanelItem(header="Managers List", content=AccountManagers())
        )
        self.add_widget(TabbedPanelItem(header="Campaigns List", content=Campaigns()))
        self.add_widget(TabbedPanelItem(header="Customers", content=Customers()))
        self.add_widget(
            TabbedPanelItem(header="Enrollments List", content=Enrollments())
        )
        self.add_widget(TabbedPanelItem(header="Product List", content=Products()))


class AccountManagers(BoxLayout):
    pass


class Campaigns(BoxLayout):
    pass


class Customers(BoxLayout):
    pass


class Enrollments(BoxLayout):
    pass


class Products(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
