from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact

@receiver(post_save, sender=Contact)
def send_email_on_save(sender, instance, created, **kwargs):
    if created:
        # Send an email with the contact form data
        pass