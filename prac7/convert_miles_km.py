from kivy.app import App, Builder

RATIO = 1.609


class ConvertMilesKm(App):

    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def increment_one(self, number):
        self.root.ids.input.text = str(int(self.root.ids.input.text) + number)

    def handle_conversion(self):
        global RATIO
        if self.root.ids.input.text == '' or self.root.ids.input.text == '-':
            self.root.ids.result.text = '0'
        elif int(self.root.ids.input.text) <= 0:
            self.root.ids.result.text = '0'
        else:
            self.root.ids.result.text = str(int(self.root.ids.input.text) * RATIO)


ConvertMilesKm().run()
