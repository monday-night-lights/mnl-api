from django.db.utils import IntegrityError

from main.management.base import DevOnlyCommand
from users.models import User


class Command(DevOnlyCommand):
    help = 'Creates a default superuser admin account for dev purposes'

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(username='admin', email=None, password='mnladmin1')
            self.stdout.write(self.style.SUCCESS("Superuser 'admin' created."))
        except IntegrityError:
            self.stdout.write(self.style.NOTICE("Superuser 'admin' already exists."))
