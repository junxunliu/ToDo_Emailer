from datetime import datetime
from typing import List, Union
from .app import App


class Checklist(App):
    def __init__(self, name: str, list_task: str,
                 tags: List[str],
                 start: Union[str, datetime],
                 due: Union[str, datetime]) -> None:

        super().__init__(name, list_task, tags, start, due)
        self.tasks = []

    def generate_email(self):
        tasks = [task.generate_email(False) for task in self.tasks]
        body = '\n'.join(tasks)

        email = super().generate_email()
        email.body = body

        return email
