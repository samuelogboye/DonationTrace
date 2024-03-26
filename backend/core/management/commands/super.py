from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()
class Command(BaseCommand):
    help = 'Create a superuser temporarily for production'

    def handle(self, *args, **options):
        username = config("ADMIN_USERNAME")
        password = config("ADMIN_PASSWORD")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, '', password)
            self.stdout.write(self.style.SUCCESS(f'Temporary superuser {username} created '))

