from textual.widgets import MarkdownViewer


class MyMarkdown(MarkdownViewer):
    def __init__(self):
        super().__init__("""# hello world""", show_table_of_contents=True)
