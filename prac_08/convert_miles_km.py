from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934

class MilesToKmApp(App):
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = 'Miles to km converter'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ""
        return self.root

    def calculate_km(self, input):
        """Convert miles to km."""
        try:
            miles = float(input)
        except ValueError:
            miles = 0.0
            self.root.ids.miles_input.text = '0.0'
        self.message = f"{miles * MILES_TO_KM_CONVERSION:.2f} km"

    def handle_increment(self, miles, direction):
        """Increment input by +1/-1 as specified and calculate km."""
        try:
            self.root.ids.miles_input.text = str(float(miles) + direction)
        except ValueError:
            self.root.ids.miles_input.text = '0.0'
        self.calculate_km(self.root.ids.miles_input.text)


MilesToKmApp().run()
