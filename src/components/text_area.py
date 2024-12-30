import pathlib

from textual.widgets import TextArea


class EditingArea(TextArea):
    def __init__(self, id: str) -> None:
        super().__init__(id=id)
        self.text = "HELLO WORLD"
        # TODO change rim color between edit mode and read only
        self.read_only = True
        self.show_line_numbers = True
        self._known_extensions_mapping = {".py": "python", ".md": "markdown"}

    def update_text(self, text_path: str) -> None:
        # fetching file extentions
        mapped_language = None
        file_extensions = pathlib.Path(text_path).suffixes
        # only handling know extentions
        if file_extensions is not None and len(file_extensions) > 0:
            for ext in file_extensions:
                mapped_language = self._known_extensions_mapping.get(ext)
                if mapped_language is None:
                    continue
                else:
                    self.language = mapped_language
        # TODO add different language suport
        with open(text_path, "r") as file_content:
            content = file_content.read()
        self.text = content
        print("-" * 100)
        print(file_extensions)
        print(mapped_language)
        print(self.language)
        print("-" * 100)

    @property
    def is_read_only(self) -> bool:
        return self.read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only: bool) -> None:
        self.read_only = is_read_only

    @property
    def is_show_line_numbers(self) -> bool:
        return self.show_line_numbers

    @is_show_line_numbers.setter
    def is_show_line_numbers(self, is_show_line_number: bool) -> None:
        self.show_line_numbers = is_show_line_number
