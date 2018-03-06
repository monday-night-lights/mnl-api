from json import loads

from urllib import parse, request

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

def clean_whitespace(text):
    return ' '.join(str(text).split())

def geocode(address):
    if settings.TESTING:
        raise ImproperlyConfigured(
            'Function venues.utils.geocode called during testing. '
            'Patch with venues.tests.mocks.mock_geocode.')

    response = request.urlopen(
        'http://maps.googleapis.com/maps/api/geocode/json' + '?' + parse.urlencode({
            'address': parse.quote_plus(address),
            'sensor': 'false'
        }))
    return loads(response.read().decode('utf8'))
