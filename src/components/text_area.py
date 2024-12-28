from textual.widgets import TextArea


class EditingArea(TextArea):
    def __init__(self, id: str) -> None:
        super().__init__(id=id)
        self.text = "HELLO WORLD"

    def update_text(self, text_path: str) -> None:
        # TODO add different language suport
        with open(text_path, "r") as file_content:
            content = file_content.read()
        self.text = content
