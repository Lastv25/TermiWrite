import os

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static

from components import FileExplorerDirTree, MyMarkdown


class DebugStatic(Static):
    def on_mount(self):
        self.update("Nothing Selected yet")

    def update_content(self, content):
        self.update(content)


class TermiWriteApp(App):
    CSS_PATH = "app.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle Dark Mode")]

    def __init__(self, folder_path: str) -> None:
        self.validate_path(folder_path)
        self._folder_path = folder_path
        super().__init__()

    @staticmethod
    def validate_path(folder_path: str) -> None:
        # expand user home directory
        expanded_path = os.path.expanduser(folder_path)
        # get the absolute path
        abs_path = os.path.abspath(expanded_path)
        # check if valid directory and if exist in the system
        if os.path.exists(abs_path):
            if os.path.isdir(abs_path):
                return None
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
        yield FileExplorerDirTree(self._folder_path, id="directory_file_tree")
        yield DebugStatic(id="body")

    def on_directory_tree_file_selected(self, event: FileExplorerDirTree.FileSelected):
        event.stop()
        target_widget = self.query_one(DebugStatic)
        target_widget.update_content(content=str(event.path))

    def on_mount(self) -> None:
        # App title in the header
        self.title = "TermiWrite"

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
