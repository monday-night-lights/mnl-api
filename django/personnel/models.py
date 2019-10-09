from django.contrib.auth.models import (AbstractUser,
                                        UserManager as DefaultUserManager)
from django.contrib.postgres.fields import ArrayField
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class UserManager(DefaultUserManager):
    # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L128
    pass


class User(AbstractUser):
    # https://github.com/django/django/blob/master/django/contrib/auth/models.py#L316
    # phone_number = PhoneNumberField(blank=True)
    nicknames = ArrayField(models.CharField(max_length=30), null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.get_full_name() or self.username


# HANDEDNESS_CHOICES = (
#     ('R', 'Right'),
#     ('L', 'Left'),
#     ('A', 'Ambidextrous'),
# )
# class Player(models.Model):
#     '''Player attributes that carry over season to season'''
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     registration_code = models.CharField(max_length=30, blank=True)
#     handedness = models.CharField(max_length=1, choices=HANDEDNESS_CHOICES)
#
#
# class Referee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     registration_code = models.CharField(max_length=30, blank=True)
