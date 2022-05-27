from fastapi import FastAPI
import uvicorn
import logging

from .utils import calculate_curve_distance
from .earthquake_API import EarthquakeAPI
from .file_writer import FileWriter

# -----------------------------------------------------------
# File name: main.py
# Author: Anand Devarajan
# Date created: 25/05/2022
# Date last modified: 25/05/2022
# Python Version: >3.9
# -----------------------------------------------------------

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# init app
app = FastAPI(debug=True)


# Routes
@app.get('/')
async def index():
    intro_str = {"Hi there": "This API is used to find the 10 earthquakes with the shortest distance "
                             "to the given geolocation"}
    return intro_str


@app.get('/geolocation')
async def get_lat_lon(Latitude, Longitude):
    try:
        Latitude = float(Latitude)
        Longitude = float(Longitude)
        # get the data from API
        api_response = EarthquakeAPI()
        response = api_response.get_response()
        if response is not None:
            json_data = response.json()
            # process the data to get the 10 nearest earthquakes
            result_lst = calculate_curve_distance(json_data, Latitude, Longitude)
            # Write the result_lst to the result.txt file.
            file_writer = FileWriter()
            file_writer.write_text(result_lst)
            return result_lst
        else:
            raise Exception("Sorry, something went wrong while fetching data.")
    except Exception as e:
        return f'{e}.'


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# docker run -v ${pwd}/data:/data  -d  --name earthquake_container -p 80:80 earthquake_img
# http://127.0.0.1/