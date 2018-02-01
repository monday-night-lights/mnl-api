from django.db import models
from django.contrib.auth.models import (AbstractUser,
                                        Group as DefaultGroup,
                                        UserManager as DefaultUserManager)


class UserManager(DefaultUserManager):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L131
    '''
    pass


class User(AbstractUser):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L288
    '''
    pass

    objects = UserManager()


class Group(DefaultGroup):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L94
    '''
    pass
