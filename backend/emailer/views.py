from emailer.email_backend import send_email
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from core.exception_handlers import ErrorEnum, ErrorResponse, response_schemas

from .models import Newsletter
from .serializers import (
    MessageSerializer,
    NewsletterSerializer,
)
from drf_spectacular.utils import extend_schema

class NewsletterView(GenericViewSet):
    serializer_class = NewsletterSerializer

    @response_schemas(
        response_model=MessageSerializer, code=201, schema_response_codes=[400]
    )
    @extend_schema(tags=['Newsletter'], summary='Subscribe to newsletter')
    def subscribe(self, request, email, **kwargs):
        #serializer = NewsletterSerializer(data=request.data)
        serializer = NewsletterSerializer(data={"email": email})

        serializer.is_valid(raise_exception=True)

        # Retrieve the validated data before saving
        validated_data = serializer.validated_data

        serializer.save()

        # Send email to the subscriber
        # Splitting the email at '@' sign and taking the first part
        subscriber_name = email.split('@')[0]
        # Prepare the HTML content from the template
        context = {'subscriber_name': subscriber_name}

        # Send email using the existing backend
        subject = 'Subscription Confirmation'
        recipient_list = [validated_data['email']]
        template = 'email/newsletter.html'

        send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)


        return Response(
            data={"detail": "email is subscribed successfully", "statusCode": 201},
            status=status.HTTP_201_CREATED,
        )

    @response_schemas(
        response_model=MessageSerializer, schema_response_codes=[404, 400]
    )
    @extend_schema(tags=['Newsletter'], summary='Unsubscribe from newsletter')
    def unsubscribe(self, request, email, **kwargs):
        serializer = NewsletterSerializer(data={"email": email})
        serializer.is_valid(raise_exception=True)

        if obj := Newsletter.objects.filter(
            email=serializer.validated_data.get("email")
        ):
            obj.delete()
            # Send email to the subscriber
            # Splitting the email at '@' sign and taking the first part
            subscriber_name = email.split('@')[0]
            # Prepare the HTML content from the template
            context = {'subscriber_name': subscriber_name}

            # Send email using the existing backend
            subject = 'Confirmation of Unsubscription'
            recipient_list = [email]
            template = 'email/unsubscribenewsletter.html'

            send_email(subject=subject, recipient_list=recipient_list, context=context, template=template)

            return Response(
                data={"detail": "email is unsubscribed successfully"},
                status=status.HTTP_200_OK,
            )

        return ErrorResponse(
            ErrorEnum.ERR_006, extra_detail="Email not subscribed previously"
        )

    @response_schemas(
        response_model=MessageSerializer, code=201, schema_response_codes=[400]
    )
    @extend_schema(tags=['Newsletter'], summary='Get list of subscribers')
    def list_subscribers(self, request, **kwargs):
        subscribers = Newsletter.objects.all()
        serializer = NewsletterSerializer(subscribers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

