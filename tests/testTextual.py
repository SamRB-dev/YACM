from textual.app import App
from textual.containers import Container
from textual.widget import Widget
from textual.reactive import Reactive
from textual.app import ComposeResult

class ResponsiveWidget(Container):
    css_class = "responsive-widget"
    
    width = Reactive(1)
    height = Reactive(1)

    def on_resize(self, event):
        self.width = self.size.width
        self.height = self.size.height
        self.refresh()

    def render(self):
        return f"Width: {self.width}, Height: {self.height}"

class MyApp(App):

    def compose(self) -> ComposeResult:
        yield ResponsiveWidget()

if __name__ == "__main__":
    MyApp().run()
