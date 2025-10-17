from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Create superuser from environment variables if not exists'

    def handle(self, *args, **kwargs):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        # Check if environment variables are provided
        if not all([username, email, password]):
            self.stdout.write('One or more environment variables are missing.')
            return

        # Check if superuser already exists
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(f'Superuser "{username}" created.')
        else:
            self.stdout.write(f'Superuser "{username}" already exists.')
