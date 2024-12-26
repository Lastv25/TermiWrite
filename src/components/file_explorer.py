from textual.widgets import DirectoryTree


class FileExplorerDirTree(DirectoryTree):
    def __init__(self, folder_path: str) -> None:
        super().__init__(folder_path)
