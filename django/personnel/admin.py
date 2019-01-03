from django.contrib import admin
from django.contrib.auth.admin import (UserAdmin as DefaultUserAdmin,
                                       GroupAdmin as DefaultGroupAdmin)
from django.contrib.auth.models import Group

from .forms import GroupAdminForm
from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    # https://github.com/django/django/blob/master/django/contrib/auth/admin.py#L42'''
    pass


admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(DefaultGroupAdmin):
    # https://github.com/django/django/blob/master/django/contrib/auth/admin.py#L26'''
    form = GroupAdminForm
