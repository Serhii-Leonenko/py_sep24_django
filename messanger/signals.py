from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.services.email_service import EmailService
from messanger.models import Message


@receiver(post_save, sender=Message)
def send_notification(sender, instance, created, **kwargs):
    if created:
        email_service = EmailService()
        email_service.send_message_created(user=instance.user, message=instance.message)
