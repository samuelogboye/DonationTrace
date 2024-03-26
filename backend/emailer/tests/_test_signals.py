# from django.contrib.auth.models import User
from core.models import User
from emailer.signals import registration_signal
from django.core import mail
import pytest

class TestSignals:
    @pytest.mark.django_db
    def test_send_welcome_email_signal(self):
        # clear mail box
        mail.outbox = []

        # Create a user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='nwankwostephen039@yahoo.com'
        )

        # Trigger the signal
        registration_signal.send(sender=User, user=user)

        # Check if the welcome email was sent
        print("After clearing:", len(mail.outbox))
        print("After clearing:",mail.outbox[0].subject)
        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == 'Thank You for Registering for Africa SME ASSEMBLY'

    def teardown_method(self, method):
        # Disconnect the signal handler after each test
        registration_signal.disconnect(sender=User)
