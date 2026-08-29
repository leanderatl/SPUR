class Content:
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def __repr__(self):
        return (
            f"Content("
            f"name={self.name!r}, "
            f"path={self.path!r}, "
            f"size={self.size!r}"
            f")"
        )