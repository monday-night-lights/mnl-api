from unittest.mock import patch

from django.test import TestCase

from .mocks import mock_geocode
from venues.models import Arena, Venue


class VenuesModelsTestCase(TestCase):

    @patch('venues.models.geocode', side_effect=mock_geocode)
    def test_venue_creation(self, patch):
        arena_1 = Arena.objects.create(name='Viking Ice Arena',
                                       address_line_1='1555 Woodward Heights',
                                       city='Hazel Park', state='MI')
        self.assertEqual(str(arena_1), 'Viking Ice Arena')
        self.assertEqual(arena_1.full_address,
                         '1555 E Woodward Heights Blvd Hazel Park Michigan 48030 US')
        self.assertEqual(arena_1.coordinates, (42.4694405, -83.0897482))

        self.assertEqual(arena_1.formatted_address,
                         '1555 E Woodward Heights Blvd, Hazel Park, MI 48030, USA')

        arena_2 = Arena.objects.create(name='Troy Sports Center',
                                       address_line_1='1819 Big Beaver',
                                       city='Troy', state='MI')
        self.assertEqual(str(arena_2), 'Troy Sports Center')

        self.assertEqual(arena_2.full_address,
                         '1819 E Big Beaver Rd Troy Michigan 48083 US')
        self.assertEqual(arena_2.coordinates, (42.5653534, -83.111801))

        self.assertEqual(arena_2.formatted_address,
                         '1819 E Big Beaver Rd, Troy, MI 48083, USA')

        venue = Venue.objects.create(name='House of Shamrocks',
                                     address_line_1='23420 John R',
                                     city='Hazel Park', state='MI')
        self.assertEqual(str(venue), 'House of Shamrocks')

        self.assertEqual(venue.full_address,
                         '23420 John R Rd Hazel Park Michigan 48030 US')
        self.assertEqual(venue.coordinates, (42.464645, -83.1037792))
        self.assertEqual(venue.formatted_address,
                         '23420 John R Rd, Hazel Park, MI 48030, USA')


    @patch('venues.models.geocode', side_effect=mock_geocode)
    def test_change_to_address_reruns_geocode(self, patch):
        arena = Arena.objects.create(name='Little Caesars Arena')
        self.assertIsNone(arena.coordinates)
        self.assertIsNone(arena.formatted_address)

        arena.address_line_1 = '2645 Woodward'
        arena.city = 'Detroit'
        arena.state = 'MI'
        arena.save()
        self.assertEqual(arena.coordinates, (42.3410478, -83.0551629))
        self.assertEqual(arena.formatted_address, '2645 Woodward Ave, Detroit, MI 48201, USA')

    @patch('venues.models.geocode', side_effect=mock_geocode)
    def test_missing_coordinates_or_formatted_address_reruns_geocode(self, patch):
        arena = Arena.objects.create(name='Little Caesars Arena',
                                     address_line_1='2645 Woodward',
                                     city='Detroit', state='MI')
        self.assertEqual(arena.coordinates, (42.3410478, -83.0551629))
        self.assertEqual(arena.formatted_address, '2645 Woodward Ave, Detroit, MI 48201, USA')

        arena.lat = None
        arena.lng = None
        arena.save()
        self.assertEqual(arena.coordinates, (42.3410478, -83.0551629))

        arena.formatted_address = None
        arena.save()
        self.assertEqual(arena.formatted_address, '2645 Woodward Ave, Detroit, MI 48201, USA')
