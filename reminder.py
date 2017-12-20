import datetime as dt
import os
import json

from dateutil import parser

from helpers import pluralize, send_mail, create_email


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
