from django.conf import settings
from django.core.management import call_command
from django.core.management.color import color_style
from django.test import TestCase
from django.utils.six import StringIO

from users.models import User


class UserCommandsTest(TestCase):

    def setUp(self):
        self.superusers = User.objects.filter(is_superuser=True)
        self.out = StringIO()
        self.color_style = color_style()

    def test_create_default_superuser_command(self):
        self.assertFalse(self.superusers.count())

        call_command('create_default_superuser', stdout=self.out)
        self.assertEquals(
            self.out.getvalue().strip(),
            self.color_style.SUCCESS("Superuser 'admin' created."))

        self.assertEqual(self.superusers.count(), 1)
        self.assertEqual(self.superusers.first().username, 'admin')

    def test_create_default_superuser_command_when_already_exists(self):
        User.objects.create_superuser(username='admin', email=None, password='testpass1')
        self.assertEqual(self.superusers.count(), 1)

        call_command('create_default_superuser', stdout=self.out)
        self.assertEquals(
            self.out.getvalue().strip(),
            self.color_style.NOTICE("Superuser 'admin' already exists."))
