from celery import shared_task

from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail(message, recipient_list):
    django_send_mail('notification', message, 'test@testmail.com', recipient_list)
