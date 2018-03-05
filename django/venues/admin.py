from django.contrib import admin

from .models import Arena, Venue
from main.admin import mnl_admin


@admin.register(Venue, site=mnl_admin)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'full_address']
    fields = [
        'name', 'phone_number',
        'address_line_1', 'address_line_2',
        'city', 'state', 'country', 'postal',
        'full_address', 'coordinates'
    ]
    readonly_fields = ['full_address', 'coordinates']


@admin.register(Arena, site=mnl_admin)
class ArenaAdmin(VenueAdmin):
    list_display = ['name', 'manager', 'phone_number', 'full_address']
    fields = [
        'name', 'manager', 'phone_number',
        'address_line_1', 'address_line_2',
        'city', 'state', 'country', 'postal',
        'full_address', 'coordinates'
    ]
