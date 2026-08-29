import os

from spur.core.content import Content
from spur.core.state import State


class Scanner:
    def scan(self, root_path):
        contents = []

        for entry in os.scandir(root_path):
            if entry.is_file():
                content = Content(
                    name=entry.name,
                    path=entry.path,
                    size=entry.stat().st_size
                )

                contents.append(content)

        return State(contents)