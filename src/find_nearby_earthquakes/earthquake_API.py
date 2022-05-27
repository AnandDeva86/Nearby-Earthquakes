import logging
import requests

# -----------------------------------------------------------
# File name: earthquake_API.py
# Author: Anand Devarajan
# Date created: 25/05/2022
# Date last modified: 25/05/2022
# Python Version: >3.9
# -----------------------------------------------------------

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class EarthquakeAPI:
    """API to call on the earthquake data """
    def __init__(self):
        self.url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

    def get_response(self):
        """Calls the earthquake_api and gets the json data"""
        try:
            response = requests.get(f'{self.url}')
            if response.ok:
                return response
            else:
                return None
        except Exception as e:
            logging.error(f'Error in API call: {e}')
            return
