import json

from spur.core.content import Content
from spur.core.state import State


class StateRepository:
    def save(self, state, file_path):
        data = []

        for content in state:
            data.append({
                "name": content.name,
                "path": content.path,
                "size": content.size
            })

        with open(file_path, "w") as file:
            json.dump(data, file)

    def load(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        contents = []

        for item in data:
            content = Content(
                name=item["name"],
                path=item["path"],
                size=item["size"]
            )

            contents.append(content)

        return State(contents)