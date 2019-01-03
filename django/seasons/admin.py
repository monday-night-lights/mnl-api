from django.contrib import admin

from .models import Season


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'duration',]
