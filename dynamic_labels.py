
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__()
        self.list_of_names = ("Bob", "Ross", "Bill")

    def build(self):
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.output_label.add_widget(temp_label)


DynamicWidgetsApp().run()
