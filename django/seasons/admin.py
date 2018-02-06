from django.contrib import admin

from .models import Season
from main.admin import mnl_admin


@admin.register(Season, site=mnl_admin)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'start_date', 'end_date',]
