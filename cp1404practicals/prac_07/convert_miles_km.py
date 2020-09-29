"""
CP1404 Practical
Kivy GUI program to covert km to miles
Benjamin Nicholson
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKms(App):
    message = StringProperty()

    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increments(self, change):
        value = self.get_valid_miles() + change
        self.root.ids.user_input.text = str(value)
        self.handle_calculation()

    def handle_calculation(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.message = self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.user_input.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKms().run()
