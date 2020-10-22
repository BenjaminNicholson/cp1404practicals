"""
CP1404 1/10/2020
Dynamically create a widget with a list of names as labels
Benjamin Nicholson
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamically created labels of names"""
    label_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.names_in_list = ["Ben", "April", "James", "Harry", "Kim"]

    def build(self):
        """Build the GUI"""
        self.title = "Dynamic Widget"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the list entries"""
        for name in self.names_in_list:
            temp_label = Label(text=name, id=name)
            temp_label.font_size = 24
            temp_label.color = (0, 1, 1, 1)
            self.root.ids.list_of_labels.add_widget(temp_label)


DynamicLabelsApp().run()
