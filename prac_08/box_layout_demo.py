from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet input name when button pressed."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_greet(self):
        """Clear writing from output label and input box."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''

BoxLayoutDemo().run()
