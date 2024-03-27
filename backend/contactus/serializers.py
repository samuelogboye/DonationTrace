from rest_framework import serializers

from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["email", "full_name", "message", "enquiry_type", "subject"]

    def create(self, validated_data):
        return ContactUs.objects.create(**validated_data)


class MessageSerializer(serializers.Serializer):
    detail = serializers.CharField()
