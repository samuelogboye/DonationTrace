from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile
from emailer.email_backend import send_email
from django.contrib.auth.signals import user_logged_in
import datetime

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance,      first_name=instance.first_name,               last_name=instance.last_name,)

        email = instance.email
        # Send email to the registered user
        subscriber_name = email.split('@')[0]
        # Prepare the HTML content from the template
        context = {'subscriber_name': subscriber_name}
        # Send email using the existing backend
        subject = 'HealthSync - Registration Alert'
        recipient_list = [email]
        template = 'email/signup_alert.html'
        send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)
    else:
        if hasattr(instance, 'userprofile'):
            instance.userprofile.first_name = instance.first_name
            instance.userprofile.last_name = instance.last_name
            instance.userprofile.save()

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

