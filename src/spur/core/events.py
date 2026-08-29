class RelocationEvent:
    def __init__(self, content_name, previous_path, current_path):
        self.content_name = content_name
        self.previous_path = previous_path
        self.current_path = current_path

    def __repr__(self):
        return (
            f"RelocationEvent("
            f"content_name={self.content_name!r}, "
            f"previous_path={self.previous_path!r}, "
            f"current_path={self.current_path!r}"
            f")"
        )