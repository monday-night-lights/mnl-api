from django.contrib import admin

from .models import Season, Team


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'duration',]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',]
