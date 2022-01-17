from datetime import date, datetime
from app.email import Email
from typing import Literal, Union, List
from dateutil.parser import parse


class App:
    def __init__(self, name: str, list_task: str,
                 start: Union[str, datetime] = None,
                 due: Union[str, datetime] = None,
                 tags: List[str] = None,
                 priority: Literal[0, 1, 2, 3] = 0) -> None:
        self.name = name
        self.list = list_task
        self.tags = tags
        self.priority = priority

        try:
            self.start_dt = parse(start) if isinstance(start, str) else start
            self.due_dt = parse(due) if isinstance(due, str) else due
        except ValueError:
            print('Incorrect date format.')

    def generate_email(self, include_options=True):

        def get_formatted_date(data_time: Union[date, datetime]) -> str:
            formatted_date = data_time.strftime('%-m-%-d-%-y')

            if isinstance(data_time, datetime):
                formatted_date += ' ' + data_time.strftime('%-I:%-M%p')

            return formatted_date

        subject = self.name

        if not include_options:
            return Email(subject)

        options = []
        if self.start_datetime:
            options.append(f'start({get_formatted_date(self.start_datetime)})')

        if self.due_datetime:
            options.append(f'due({get_formatted_date(self.due_datetime)})')

        if self.priority:
            priority_symbol = self.priority * '!'
            options.append(f'priority({priority_symbol})')

        if self.list:
            options.append(f'list({self.list})')

        if self.tags:
            tags_list = ','.join(self.tags)
            options.append(f'tag({tags_list})')

        subject += ' ' + ' '.join(options)

        return Email(subject)
