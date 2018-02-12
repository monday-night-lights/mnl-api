GEOCODE_RESPONSES = {
    '1555 Woodward Heights Hazel Park MI': {
        'status': 'OK',
        'results': [{
            'address_components': [
                {'short_name': '1555', 'types': ['street_number']},
                {'short_name': 'E Woodward Heights Blvd', 'types': ['route']},
                {'short_name': 'Hazel Park', 'types': ['locality', 'political']},
                {'long_name': 'Michigan', 'types': ['administrative_area_level_1', 'political']},
                {'short_name': 'US', 'types': ['country', 'political']},
                {'short_name': '48030', 'types': ['postal_code']},
            ],
            'formatted_address': '1555 E Woodward Heights Blvd, Hazel Park, MI 48030, USA',
            'geometry': {'location': {'lng': -83.0897482, 'lat': 42.4694405}}
        }]
    },
    '1819 Big Beaver Troy MI': {
        'status': 'OK',
        'results': [{
            'address_components' : [
                {'short_name': '1819', 'types': ['street_number']},
                {'short_name': 'E Big Beaver Rd', 'types': ['route']},
                {'short_name': 'Troy', 'types': ['locality', 'political']},
                {'long_name': 'Michigan', 'types': ['administrative_area_level_1', 'political']},
                {'short_name': 'US', 'types': ['country', 'political']},
                {'short_name': '48083', 'types': ['postal_code']},
            ],
            'formatted_address': '1819 E Big Beaver Rd, Troy, MI 48083, USA',
            'geometry': {'location': {'lng': -83.111801, 'lat': 42.5653534}}
        }]
    },
    '23420 John R Hazel Park MI': {
        'status': 'OK',
        'results': [{
            'address_components': [
                {'short_name': '23420', 'types': ['street_number']},
                {'short_name': 'John R Rd', 'types': ['route']},
                {'short_name': 'Hazel Park', 'types': ['locality', 'political']},
                {'long_name': 'Michigan', 'types': ['administrative_area_level_1', 'political']},
                {'short_name': 'US', 'types': ['country', 'political']},
                {'short_name': '48030', 'types': ['postal_code']},
            ],
            'formatted_address': '23420 John R Rd, Hazel Park, MI 48030, USA',
            'geometry': {'location': {'lng': -83.1037792, 'lat': 42.464645}}
        }]
    },
}

def mock_geocode(address):
    # usage:
    #     from unittest.mock import patch
    #     from venues.tests.mocks import mock_geocode

    #     @patch('venues.models.geocode', side_effect=mock_geocode)
    #     def test_venue_creation(self, patch):
    try:
        return GEOCODE_RESPONSES[address]
    except KeyError:
        return {'status': 'ZERO_RESULTS', 'results': []}
