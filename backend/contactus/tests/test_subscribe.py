# (Arrange, Act, Assert) - AAA


import pytest
from faker import Faker
from model_bakery import baker
from rest_framework import status

from core.exception_handlers import ErrorEnum
from emailer.models import Newsletter

FAKE = Faker()


@pytest.mark.django_db
class TestSubscribe:
    def test_successful_subsription_returns_201(self, api_client):
        email = FAKE.email()
        response = api_client.post("/api/v1/subscribe", data={"email": email})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["detail"] == "email is subscribed successfully"

    def test_invalid_email_passed_returns_400(self, api_client):
        response = api_client.post("/api/v1/subscribe", data={"email": "wrong email"})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error_code"] == ErrorEnum.ERR_001.name

    def test_duplicate_subscription_returns_400(self, api_client):
        email = FAKE.email()
        baker.make(Newsletter, email=email)

        response = api_client.post("/api/v1/subscribe", data={"email": email})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["detail"][0]["msg"] == "email already subscribed"


@pytest.mark.django_db
class TestUnSubscribe:
    def test_successful_unsubsribe_action_returns_200(self, api_client):
        email = FAKE.email()
        baker.make(Newsletter, email=email)

        response = api_client.delete(
            f"/api/v1/unsubscribe/{email}",
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["detail"] == "email is unsubscribed successfully"

    def test_invalid_email_passed_returns_400(self, api_client):
        email = "invalid email"
        response = api_client.delete(
            f"/api/v1/unsubscribe/{email}",
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error_code"] == ErrorEnum.ERR_001.name

    def test_email_not_previously_subscribed_returns_404(self, api_client):
        email = FAKE.email()

        response = api_client.delete(
            f"/api/v1/unsubscribe/{email}",
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["error_code"] == ErrorEnum.ERR_006.name
