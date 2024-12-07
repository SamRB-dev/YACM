from components.classes.HeaderFooter import AppHeader
from textual.app import App, ComposeResult

class main(App):
    CSS_PATH = "components/terminalCSS/style.tcss"
    def compose(self) -> ComposeResult:
        yield AppHeader()
        
    def _on_compose(self):
        self.title = "Yet Another Clipboard Manager"

if __name__ == "__main__":
    try:
        main().run()
    except Exception as error:
        print(error)