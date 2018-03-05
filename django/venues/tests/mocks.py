def geocode_response(street_number, route, locality, admin_area_1, country,
                     postal_code, formatted_address, lng, lat):
    return {
        'status': 'OK',
        'results': [{
            'address_components': [
                {'short_name': street_number, 'types': ['street_number']},
                {'short_name': route, 'types': ['route']},
                {'short_name': locality, 'types': ['locality', 'political']},
                {'long_name': admin_area_1, 'types': ['administrative_area_level_1', 'political']},
                {'short_name': country, 'types': ['country', 'political']},
                {'short_name': postal_code, 'types': ['postal_code']},
            ],
            'formatted_address': formatted_address,
            'geometry': {'location': {'lng': lng, 'lat': lat}}
        }]
    }

VIKING_ICE_ARENA = geocode_response(
    '1555', 'E Woodward Heights Blvd', 'Hazel Park', 'Michigan', 'US', '48030',
    '1555 E Woodward Heights Blvd, Hazel Park, MI 48030, USA', -83.0897482, 42.4694405)
TROY_SPORTS_CENTER = geocode_response(
    '1819', 'E Big Beaver Rd', 'Troy', 'Michigan', 'US', '48083',
    '1819 E Big Beaver Rd, Troy, MI 48083, USA', -83.111801, 42.5653534)
HOUSE_OF_SHAMROCKS = geocode_response(
    '23420', 'John R Rd', 'Hazel Park', 'Michigan', 'US', '48030',
    '23420 John R Rd, Hazel Park, MI 48030, USA', -83.1037792, 42.464645)
LITTLE_CAESARS_ARENA = geocode_response(
    '2645', 'Woodward Ave', 'Detroit', 'Michigan', 'US', '48201',
    '2645 Woodward Ave, Detroit, MI 48201, USA', -83.0551629, 42.3410478)

GEOCODE_RESPONSES = {
    '1555 Woodward Heights Hazel Park MI': VIKING_ICE_ARENA,
    '1819 Big Beaver Troy MI': TROY_SPORTS_CENTER,
    '23420 John R Hazel Park MI': HOUSE_OF_SHAMROCKS,
    '2645 Woodward Detroit MI': LITTLE_CAESARS_ARENA,
    '2645 Woodward Ave Detroit Michigan 48201 US': LITTLE_CAESARS_ARENA,
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
