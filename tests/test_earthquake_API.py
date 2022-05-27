import unittest
from unittest.mock import patch
from src.find_nearby_earthquakes.earthquake_API import EarthquakeAPI


class TestApiCall(unittest.TestCase):

    @patch('src.find_nearby_earthquakes.earthquake_API.requests.get')
    def test_success_get_response(self, mock_get):
        dummy_json = {"result": {'value': 'Hello There!'}}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = dummy_json

        eq = EarthquakeAPI()
        res = eq.get_response()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), dummy_json)

    @patch('src.find_nearby_earthquakes.earthquake_API.requests.get')
    def test_fail_get_response(self, mock_get):

        mock_get.return_value.status_code = 403
        mock_get.return_value.json.return_value = None

        eq = EarthquakeAPI()
        res = eq.get_response()

        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.json(), None)


if __name__ == '__main__':
    unittest.main()
