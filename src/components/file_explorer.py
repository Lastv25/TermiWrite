from textual.widgets import DirectoryTree


class FileExplorerDirTree(DirectoryTree):
    ICON_NODE_EXPANDED = "▾ "
    ICON_NODE = "▸ "
    ICON_FILE = "⦁ "  # Remove icons in the result

    def __init__(self, folder_path: str, id: str = None) -> None:
        super().__init__(folder_path, id=id)
