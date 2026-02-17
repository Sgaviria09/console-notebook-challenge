

from datetime import datetime

class Note:

    HIGH: str = "high"
    MEDIUM: str = "medium"
    LOW: str = "low"

def __init__(self, code: str, title: str, text: str, importance:str):
    self.code: str = code
    self.title: str = title
    self.text: str = text
    self.importance: str = importance
    self.creation_date = datetime.now()
    self.tag: list[str] = []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    return f"Date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:

    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        code = len(self.notes) +

