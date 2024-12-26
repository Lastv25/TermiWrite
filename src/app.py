from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from components import MyMarkdown


class TermiWriteApp(App):

    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield MyMarkdown()

    def on_mount(self):
        # App title in the header
        self.title = "TermiWrite"

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
