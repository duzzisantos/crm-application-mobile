from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton


class ActionButton(BoxLayout):
    def __init__(self, manager_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"

        for key, value in manager_data.items():
            self.add_widget(Label(text=str(value)))

        delete_button = MDRaisedButton(
            text="Delete", size_hint=[None, None], size=(80, 30)
        )
        delete_button.bind(
            on_release=lambda x: self.delete_manager(manager_data["accountManagerId"])
        )
        self.add_widget(delete_button)

    def delete_manager(self, manager_id):
        print(f"Deleting manager with ID: {manager_id}")
