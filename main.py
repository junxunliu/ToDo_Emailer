from typing import List, Union

from app import Emailer
from models import App, Checklist

TASK_LISTS = ["Home", "School/Coop", "Side Projects"]


class Todo:
    def __init__(self):
        self.emailer = Emailer()

    def send_email(self):
        self.emailer.send_email()

    def add_task(self, task_name: Union[App, Checklist]):
        self.emailer.add_email(task_name.generate_email())

    def get_tasks(self):
        task_list: List[Union[App, Checklist]] = []
        emails = [email.generate_email() for email in task_list]
        self.emailer.emails = emails


if __name__ == '__main__':
    todo = Todo()
    tasks = []

    for task in tasks:
        todo.add_task(task)

    todo.send_email()
