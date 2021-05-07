from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_to_number(self, text):
        try:
            return float(text)
        except ValueError:
            return 0.0

    def handle_calculate(self, text):
        print("calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        print("increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.miles_input.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KM)


MilesConverterApp().run()