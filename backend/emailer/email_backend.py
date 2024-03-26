import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        super().__init__(group=None)

    def run(self):
        self.email.send()

def send_email(
    subject: str,
    recipient_list: list,
    message: str = None,
    context: dict = {},
    template: str = None,
):
    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email for email in recipient_list],
    )

    if template:
        html_content = render_to_string(template, context)

        email.attach_alternative(html_content, "text/html")

    # start a thread for each email
    try:
        EmailThread(email).start()

    except ConnectionError:
        print("Something went wrong \nCouldn't send Email")
