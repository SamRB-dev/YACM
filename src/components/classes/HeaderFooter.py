from textual.widgets import Header, Footer

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

class AppFooter(Footer):
    pass