from kivy.app import App
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard

class ClipboardApp(App):
    def build(self):
        clip = Clipboard.get_text()
        return Label(text=clip)

if __name__ == "__main__":
    ClipboardApp().run()
