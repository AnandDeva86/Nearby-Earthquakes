"""""""""""""""""
Nearby Earthquakes
"""""""""""""""""

A simple FastAPI application.

.. contents:: Overview
   :depth: 3

Description
============

This is a simple FastAPI application which is used to calculate the nearest 10 earthquakes from a given latitude and longitude.
The application fetches the list of earthquakes that happened during last 30 days from `USGS <https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson>`_.
Calculates the distance between the given latitude and longitude with    each of the earthquakes using Haversine Formula.
Removes the duplicate latitude and longitude, when two earthquakes happened in exactly the same location.
Returns 10 earthquakes with the shortest distance to the given city.

Getting Started
============

Dependencies
----------
- Poetry
- Docker
- pandas
- numpy
- uvicorn
- FastAPI

Executing program
----------
- Build the docker image with a name

``docker build -t <image_name> .``

- Create and run a container with

``docker run -v ${pwd}/data:/data  -d  --name <container_name> -p 80:80 <image_name>``

- Open the `local host <http://127.0.0.1/docs>`_ and in the swagger UI give the latitude and longitude in the response body.

- The result is saved in the ./data/Result.txt.


Authors
============
`Anand Devarajan <https://www.linkedin.com/in/ananddevarajan>`_

Version History
============

* 0.1
    * Initial Release

License
============

see the LICENSE.md file for details