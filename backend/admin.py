import os
import django
from django.contrib.auth.models import User

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthsync.settings')
django.setup()


def create_admin_user():
    # Create a new user
    new_user = User.objects.create_user(username='sam', email='ogboyesam@gmail', password='test')

    # Add admin privileges to the user
    new_user.is_staff = True
    new_user.is_superuser = True
    new_user.save()

if __name__ == "__main__":
    create_admin_user()
