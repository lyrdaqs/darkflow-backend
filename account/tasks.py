from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(title, text, sender, receiver):
    send_mail(
        title,
        text,
        sender,
        [receiver]
    )