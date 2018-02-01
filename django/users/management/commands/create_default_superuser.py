from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from users.models import User


class Command(BaseCommand):
    help = 'Creates a default superuser admin account'

    def handle(self, **options):
        try:
            user = User.objects.create_superuser(username='admin', email=None, password='mnladmin1')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created."))
        except IntegrityError:
            self.stdout.write(self.style.NOTICE("Superuser 'admin' already exists."))
