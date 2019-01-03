from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

from .utils import clean_whitespace, geocode
from main.logging import logger


class Location(models.Model):
    address_line_1 = models.CharField(max_length=60, blank=True)
    address_line_2 = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=20, blank=True, verbose_name='State/Province')
    country = models.CharField(max_length=50, blank=True)
    postal = models.CharField(max_length=10, blank=True)

    formatted_address = models.CharField(max_length=300, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not (self.pk and self.coordinates and self.formatted_address):
            self.geocode_address()
        else:
            existing = self.__class__.objects.get(pk=self.pk)
            address_changed = (
                existing.address_line_1 != self.address_line_1 or
                existing.address_line_2 != self.address_line_2 or
                existing.city != self.city or
                existing.state != self.state or
                existing.postal != self.postal or
                existing.country != self.country)
            if address_changed:
                self.geocode_address()
        super().save(*args, **kwargs)

    @property
    def coordinates(self):
        if self.lat and self.lng:
            return (self.lat, self.lng)
        return None

    @property
    def full_address(self):
        return clean_whitespace(' '.join([
            self.address_line_1, self.address_line_2,
            self.city, self.state, self.postal, self.country,
        ]))

    def geocode_address(self):
        def find(address_components, component_type, verbose=False):
            return next(
                filter(lambda c: component_type in c['types'], address_components),
                {}).get('long_name' if verbose else 'short_name',  '')

        if not self.full_address:
            return

        data = geocode(self.full_address)
        logger.info('Geocoding "{address}"\n{response}'.format(
            address=self.full_address, response=data))

        if data['status'] == 'OK':
            result = data['results'][0]
            self.lat = result['geometry']['location']['lat']
            self.lng = result['geometry']['location']['lng']
            self.formatted_address = result['formatted_address']

            components = result['address_components']
            self.address_line_1 = clean_whitespace(
                find(components, 'street_number') + ' ' +
                find(components, 'route'))
            self.city = find(components, 'locality')
            self.state = find(components, 'administrative_area_level_1', True)
            self.postal = find(components, 'postal_code')
            self.country = find(components, 'country')


class Venue(Location):
    '''Used for arenas and other meetings places e.g. bars'''
    name = models.CharField(max_length=40)
    # phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name


class Arena(Venue):
    manager = models.CharField(max_length=40, blank=True,
                               help_text='Contact person at the arena')


# Rink
#    arena (FK)
#    number
#    name (optional)


# LockerRoom
#    rink (FK)
#    number
#    name (optional)
