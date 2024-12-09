from textual.widgets import Header, Footer, Static, Link
from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Horizontal, Container
from textual.reactive import Reactive

class AppHeader(Header):
    def __init__(self):
        self.__showClock: bool = True
        self.__showIcon: str | None = "YACM"
        self.__isTall: bool = True
        super().__init__(
            show_clock=self.__showClock,
            icon=self.__showIcon
        )
        
    def _on_mount(self):
        self.tall = self.__isTall

class AppFooter(Container):
    width = Reactive(1)
    height = Reactive(1)
    def compose(self) -> ComposeResult:
        # yield Link (
        #     text="Github",  
        #     url="www.google.com",
        #     classes="github"
        # )
        yield Static("Github", classes="github")
        yield Static("v1.0", classes="version")
    def _on_compose(self):
        self.classes = "AppFooter"
    
        