import os

from components import MyMarkdown
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class TermiWriteApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def __init__(self, folder_path: str) -> None:
        self.validate_path(folder_path)
        super().__init__()

    @staticmethod
    def validate_path(folder_path: str) -> bool:
        # expand user home directory
        expanded_path = os.path.expanduser(folder_path)
        # get the absolute path
        abs_path = os.path.abspath(expanded_path)
        # check if valid directory and if exist in the system
        if os.path.exists(abs_path):
            if os.path.isdir(abs_path):
                return True
            else:
                raise ValueError(
                    f"The path passed in input is not a directory: {abs_path}"
                )
        else:
            raise ValueError(
                f"The path passed in input does not exist on the machine: {abs_path}"
            )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        # yield MyMarkdown()

    def on_mount(self) -> None:
        # App title in the header
        self.title = "TermiWrite"

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
