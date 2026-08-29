class State:
    def __init__(self, contents=None):
        self.contents = contents if contents is not None else []

    def add(self, content):
        self.contents.append(content)

    def __len__(self):
        return len(self.contents)

    def __iter__(self):
        return iter(self.contents)