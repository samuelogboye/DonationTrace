# import datetime

# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from customauth.models import CustomUser
# from faker import Faker

# from attendee_kyc.models import AttendeeKYC
# from emailer.email_backend import send_email
# from ticketing_app.models import BookTicket, ExhibitionTicket
# from emailer.models import Newsletter


# @receiver(post_save, sender=AttendeeKYC)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         subject = "Thank You for Registering with us"
#         message = "registration_email_message"
#         recipient_list = [instance.email]
#         context = {
#             "name": instance.full_name,
#             "venue": Faker().address(),
#             "time": datetime.datetime.now().time(),
#             "contact_email": settings.DEFAULT_FROM_EMAIL,
#         }
#         Newsletter.objects.get_or_create(email=instance.email)
#         send_email(
#             subject=subject,
#             message=message,
#             recipient_list=recipient_list,
#             template="email/registration.html",
#             context=context,
#         )


# @receiver(post_save, sender=ExhibitionTicket)
# def send_email_for_exhibition(sender, instance, created, **kwargs):
#     if created:
#         subject = "Your Exhibition ticket has been booked successfully"
#         message = subject
#         recipient_list = [instance.email]
#         context = {
#             "full_name": instance.full_name,
#             "business_name": instance.business_name,
#             "country": instance.country,
#             "ticket_ref_number": instance.ticket_ref_number,
#             "contact_email": settings.DEFAULT_FROM_EMAIL,
#             "venue": Faker().address(),
#             "time": datetime.datetime.now().time(),
#         }
#         Newsletter.objects.get_or_create(email=instance.email)

#         send_email(
#             subject=subject,
#             message=message,
#             recipient_list=recipient_list,
#             context=context,
#             template="email/exhibition_ticket.html",
#         )


# @receiver(post_save, sender=BookTicket)
# def send_email_for_booking(sender, instance, created, **kwargs):
#     if created:
#         subject = "Your Ticket has been booked"
#         message = "Your ticket  for the ASME 2023 event has been booked successfully"
#         recipient_list = [instance.email]
#         context = {
#             "full_name": instance.full_name,
#             "business_name": instance.business_name,
#             "country": instance.country,
#             "ticket_ref_number": instance.ticket_ref_number,
#             "contact_email": settings.DEFAULT_FROM_EMAIL,
#             "venue": Faker().address(),
#             "time": datetime.datetime.now().time(),
#         }
#         Newsletter.objects.get_or_create(email=instance.email)

#         send_email(
#             subject=subject,
#             message=message,
#             recipient_list=recipient_list,
#             context=context,
#             template="email/book_ticket.html",
#         )

# @receiver(post_save, sender=CustomUser)
# def send_registration_email(sender, instance, created, **kwargs):
#     if created:  # Check if a new user is created
#         email = instance.email
#         # Send email to the registered user
#         subscriber_name = email.split('@')[0]
#         # Prepare the HTML content from the template
#         context = {'subscriber_name': subscriber_name}
#         # Send email using the existing backend
#         subject = 'Donation Trace - Registration Alert'
#         recipient_list = [email]
#         template = 'email/signup_alert.html'
#         send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)

