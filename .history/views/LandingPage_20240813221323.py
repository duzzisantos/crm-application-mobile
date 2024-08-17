from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2

        self.managerBtn = Button(text="Account Managers", font_size=40)
        self.add_widget(self.managerBtn)
        self.campaignBtn = Button(tetx="Campaigns", font_size=40)
        self.add_widget(self.campaignBtn)
        self.customersBtn = Button(text="Customers", font_size=40)
        self.add_widget(self.customersBtn)
        self.enrollmentBtn = Button(text="Enrollments", font_size=40)
        self.add_widget(self.enrollmentBtn)
        self.productsBtn = Button(text="Products", font_size=40)
        self.add_widget(self.productsBtn)


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
