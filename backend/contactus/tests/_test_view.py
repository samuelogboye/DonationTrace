from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestEmailSendingView:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()
        self.send_email_url = reverse("send-email")

    def test_send_email(self):
        email_data = {
            "to_email": "nwankwostephen039@yahoo.com",
            "subject": "Test Email Subject",
            "message": "This is a test email message.",
        }

        response = self.client.post(self.send_email_url, email_data, format="json")

        # Check if the email was sent successfully
        assert response.status_code == status.HTTP_200_OK
        assert response.data["message"] == "Email sent successfully."

    def test_send_email_invalid_data(self):
        # Define invalid email data (missing required fields)
        invalid_email_data = {
            "subject": "Test Email Subject",
        }

        response = self.client.post(
            self.send_email_url, invalid_email_data, format="json"
        )

        # Check for a bad request response
        assert response.status_code == status.HTTP_400_BAD_REQUEST
