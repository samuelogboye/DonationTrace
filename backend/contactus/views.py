from emailer.email_backend import send_email
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from core.exception_handlers import ErrorEnum, ErrorResponse, response_schemas

from .models import ContactUs
from .serializers import ContactUsSerializer, MessageSerializer
from drf_spectacular.utils import extend_schema

class ContactUsView(GenericViewSet):
    serializer_class = ContactUsSerializer

    @response_schemas(
        response_model=MessageSerializer, code=201, schema_response_codes=[400]
    )
    @extend_schema(tags=['Contact Us'], summary='Contact Us using email')
    def contactus(self, request, **kwargs):
        #serializer = NewsletterSerializer(data=request.data)
        serializer = ContactUsSerializer(data={"email": request.data['email'], "full_name": request.data['full_name'], "message": request.data['message'], "enquiry_type": request.data['enquiry_type'], "subject": request.data['subject']})

        serializer.is_valid(raise_exception=True)

        # Retrieve the validated data before saving
        validated_data = serializer.validated_data

        serializer.save()

        # Send email to the contact
        # Prepare the HTML content from the template
        context = {'full_name': validated_data['full_name'], 'message': validated_data['message'], 'enquiry_type': validated_data['enquiry_type'], 'subject': validated_data['subject'], 'email': validated_data['email']}

        # Send email to the person who submitted the form
        subject = 'We received your enquiry'
        recipient_list = [validated_data['email']]
        template = 'email/contact_sender.html'

        # Send email to Admin
        subject_admin = 'New Enquiry'
        admin_email = ['ogboyesam@gmail.com']
        template_admin = 'email/contact_admin.html'

        send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)

        # Admin
        send_email(subject=subject_admin, recipient_list=admin_email, context=context, template=template_admin)


        return Response(
            data={"detail": "Contact details received and email sent", "statusCode": 201},
            status=status.HTTP_201_CREATED,
        )
