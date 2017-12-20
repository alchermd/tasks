import smtplib
from email.mime.text import MIMEText


def pluralize(text: str, amount: int) -> str:
    """'Pluralizes' a string if a given amount is plural.
    Example:
        pluralize('egg', 2) -> 'eggs'
        pluralize('python', 1) ->
    """
    return text + 's' if amount > 1 else text


def create_email(subject: str, _from: str, to: str, body: str) -> MIMEText:
    """Generates an email object from the given parameters. """
    email = MIMEText(body)
    email['Subject'] = subject
    email['From'] = _from
    email['To'] = to

    return email


def send_mail(email: MIMEText, email_address: str, password: str):
    """Creates a new SMTP connection and sends a new email."""
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()
    s.login(email_address, password)
    s.send_message(email)

    s.quit()
