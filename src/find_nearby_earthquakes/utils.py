import numpy as np
import pandas as pd
import logging

# -----------------------------------------------------------
# File name: utils.py
# Author: Anand Devarajan
# Date created: 25/05/2022
# Date last modified: 25/05/2022
# Python Version: >3.9
# -----------------------------------------------------------


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def generate_df_from_json(json_data):
    """This function parses the json url and returns a dataframe with Latitude,Longitude and Title """
    # convert json to dataframe
    df = pd.json_normalize(json_data['features'])
    # filter only earthquake data
    df = df[df['properties.type'] == 'earthquake']
    df.reset_index(drop=True, inplace=True)

    # create a new dataframe with lat, lan and title columns
    df_new = pd.DataFrame()
    for i in range(len(df)):
        lst = df['geometry.coordinates'].iloc[i]
        lon = lst[0]
        lat = lst[1]
        title = df['properties.title'][i]
        dframe = pd.DataFrame([lat, lon, title])
        dframe = dframe.T
        df_new = pd.concat([df_new, dframe])
    df_new.reset_index(drop=True, inplace=True)
    df_new = df_new.rename(columns={0: 'Latitude', 1: 'Longitude', 2: 'Title'})
    return df_new


def haversine_distance(lat1, lon1, lat2, lon2):
    """This function uses the Haversine Formula to calculate distance between two coordinates on a sphere
                                                                        from esri Community."""
    # r is the radius of the earth in km
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    disc = round(r * c)
    return int(disc)


def calculate_curve_distance(json_data, lat1, lon1):
    """This function calculates the distance between the given input coordinates and
                                            each of the earthquakes and returns the nearst 10 locations"""
    df = generate_df_from_json(json_data)
    df['Distance'] = 0
    # calculate the distance between the given city and each of the lat/lon in the dataframe
    # and store in a new column called Distance
    for i in range(len(df)):
        lat2 = df['Latitude'].iloc[i]
        lon2 = df['Longitude'].iloc[i]
        disc = haversine_distance(lat1, lon1, lat2, lon2)
        df['Distance'].iloc[i] = round(disc)
    # remove duplicate lat/lon
    df.drop_duplicates(subset=['Latitude', 'Longitude'], keep='first', inplace=True)
    # filter the 10 earthquakes with the shortest distance(kilometres) to the given city
    df1 = df.sort_values(by='Distance', ascending=True).head(10)

    # create a list for the 10 values with content of a title field followed by || and distance
    result_lst = []
    for i in range(len(df1)):
        title = df1['Title'].iloc[i]
        distance = df1['Distance'].iloc[i]
        result_lst.append(f'{title} || {distance}')
    return result_lst
