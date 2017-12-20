import datetime as dt
import os

from dateutil import parser

from helpers import pluralize, send_mail, create_email


def main():
    deadline = parser.parse(os.getenv('DEADLINE'))
    deadline_desc = os.getenv('DEADLINE_DESC')

    difference = (deadline.date() - dt.date.today()).days

    if difference <= 7:
        body = (
            f"""
                {difference} {pluralize('day', difference)} left -> '{deadline_desc}'.
                Sent by {os.path.basename(__file__)}.
            """
        )
        email = create_email('Reminder', os.getenv('EMAIL'), os.getenv('EMAIL'), body)
        send_mail(email)


if __name__ == '__main__':
    main()
