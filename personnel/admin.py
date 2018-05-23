from django.contrib import admin
from django.contrib.auth.admin import (UserAdmin as DefaultUserAdmin,
                                       GroupAdmin as DefaultGroupAdmin)

from .forms import GroupAdminForm
from .models import Group, User
from main.admin import mnl_admin


@admin.register(User, site=mnl_admin)
class UserAdmin(DefaultUserAdmin):
    '''https://github.com/django/django/blob/master/django/contrib/auth/admin.py#L42'''
    pass


@admin.register(Group, site=mnl_admin)
class GroupAdmin(DefaultGroupAdmin):
    '''https://github.com/django/django/blob/master/django/contrib/auth/admin.py#L26'''
    form = GroupAdminForm
