

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y

@shared_task
def send_periodic_email():
    send_mail(
        subject='Salom!',
        message='Bu 5 ',
        from_email='khushvaqt.arab@gmail.com',
        recipient_list=['xushvaqt.abdigafforov@gmail.com'],
        fail_silently=False
    )