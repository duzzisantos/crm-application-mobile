from kivy.app import App
from views import LandingPage


class Main(App):
    def build(self):
        return LandingPage()


if __name__ == "__main__":
    Main().run()
