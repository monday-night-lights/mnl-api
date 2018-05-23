from django.conf import settings
from django.core.management.base import BaseCommand


class DevOnlyCommand(BaseCommand):

    def handle(self, *args, **options):
        if settings.DEBUG == False and not settings.TESTING:
            self.stdout.write(self.style.NOTICE(
                'This command is not intended for use in production.'))
            return

        super().handle(*args, **options)
