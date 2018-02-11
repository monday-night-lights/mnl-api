from django.contrib.auth.models import (AbstractUser,
                                        Group as DefaultGroup,
                                        UserManager as DefaultUserManager)

# Why override these classes?
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

    objects = UserManager()


class Group(DefaultGroup):
    '''
    https://github.com/django/django/blob/master/django/contrib/auth/models.py#L94
    '''
    pass
