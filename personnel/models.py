from django.contrib.auth.models import (AbstractUser,
                                        Group as DefaultGroup,
                                        UserManager as DefaultUserManager)
from django.contrib.postgres.fields import ArrayField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

HANDEDNESS_CHOICES = (
    ('R', 'Right'),
    ('L', 'Left'),
    ('A', 'Ambidextrous'),
)

# Why override the default auth classes?
#
# The Django docs recommend creating a custom user model at the start of a project
# if there is any chance you will want to customize the user model down the road.
# https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
class UserManager(DefaultUserManager):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L131
    '''
    pass


class User(AbstractUser):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L288
    '''
    phone_number = PhoneNumberField(blank=True)
    nicknames = ArrayField(models.CharField(max_length=30), null=True, blank=True)
    objects = UserManager()


class Group(DefaultGroup):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L94
    '''
    pass


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
