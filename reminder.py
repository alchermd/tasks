import datetime as dt
import json
import os

from dateutil import parser

from helpers import create_email, pluralize, send_mail


def main():
    CONFIG = json.load(open('config.json'))

    deadline = parser.parse(CONFIG['DEADLINE'])
    difference = (deadline.date() - dt.date.today()).days

    if difference <= 7:
        body = (
            f"""
                {difference} {pluralize('day', difference)} left -> '{CONFIG['DEADLINE_DESC']}'.
                Sent by {os.path.basename(__file__)}.
            """
        )
        email = create_email('Reminder', CONFIG['EMAIL'], CONFIG['EMAIL'], body)
        send_mail(email, CONFIG['EMAIL'], CONFIG['PASSWORD'])


if __name__ == '__main__':
    main()
