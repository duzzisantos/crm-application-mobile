from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class LandingPage(GridLayout):
    def __init__(self, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        self.cols = 2

        self.orientation = "lr-tb"

        self.label = Label(text="Good Day Admin", font_size=40)
        self.add_widget(self.label)
        self.managerBtn = Button(text="Account Managers", font_size=40)
        self.add_widget(self.managerBtn)
        self.campaignBtn = Button(text="Campaigns", font_size=40)
        self.add_widget(self.campaignBtn)
        self.customersBtn = Button(text="Customers", font_size=40)
        self.add_widget(self.customersBtn)
        self.enrollmentBtn = Button(text="Enrollments", font_size=40)
        self.add_widget(self.enrollmentBtn)
        self.productsBtn = Button(text="Products", font_size=40)
        self.add_widget(self.productsBtn)
        self.yahooFinance = Button(text="Yahoo Finance", font_size=40)
        self.add_widget(self.yahooFinance)


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    MyApp().run()
