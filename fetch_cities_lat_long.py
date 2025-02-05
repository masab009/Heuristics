"""
this is a command line tool that figures out
shortest distances between cities

"""


import geopy
import geopy.distance
import pandas as pd
import numpy as np
from random import shuffle
import click
def create_cities_dataframe():
    cities = [
        "Karachi",
        "Lahore", 
        "Faisalabad", 
        "Rawalpindi", 
        "Multan", 
        "Gujranwala", 
        "Peshawar", 
        "Quetta", 
        "Sialkot", 
        "Islamabad", 
        "Bahawalpur", 
        "Sargodha", 
        "Sukkur", 
        "Larkana", 
        "Sheikhupura", 
        "Jhang", 
        "Dera Ghazi Khan", 
        "Gujrat", 
        "Mardan", 
        "Kasur", 
        "Rahim Yar Khan", 
        "Sahiwal", 
        "Okara", 
        "Wah Cantonment", 
        "Mingora", 
        "Mirpur Khas", 
        "Chiniot", 
        "Nawabshah", 
        "Kamoke", 
        "Burewala"
    ]
    latitude = []
    longitude = []
    geolocator = geopy.geocoders.Nominatim(user_agent = "tsp_pandas")
    for city in cities:
        
        location = geolocator.geocode(city)
        latitude.append(location.latitude)
        longitude.append(location.longitude)

    df = pd.DataFrame(
        {
            "cities":cities,
            "latitudes" : latitude,
            "longitudes":longitude
        }
    )
    return df


def calculate_distance(lat1,lat2,lon1,lon2):
    # converting the received angles from degree to radians
    R = 6371
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    lon1 = np.radians(lon1)
    lon2 = np.radians(lon2)
    lat_d = lat2-lat1
    lon_d = lon2 - lon1
    a = np.sin(lat_d / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(lon_d / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    distance = R*c
    return distance



def tsp(cities_df):
    city_list = cities_df.sample(frac=1).reset_index(drop=True)  # Shuffle cities & coordinates

    print(f"The cities have been randomized in the following order: {city_list['cities'].tolist()}")

    total_distance = 0
    for i in range(len(city_list) - 1):
        total_distance += calculate_distance(
            city_list.loc[i, "latitudes"], city_list.loc[i + 1, "latitudes"],
            city_list.loc[i, "longitudes"], city_list.loc[i + 1, "longitudes"]
        )

    return total_distance, city_list["cities"].tolist()

@click.command()
@click.option("--simulations",type=int, default=10,help="number of arguements to pass")
def main(simulations):
    distance_list  = []
    city_list_list = []
    cdf = create_cities_dataframe()
    for i in range(simulations):
        distance, city_list = tsp(cdf)
        print(f"runing simulation number {i}: found the distance {distance}")
        distance_list.append(distance)
        city_list_list.append(city_list)

    shortest_distance_index = distance_list.index(min(distance_list))
    print("Shortest Distance: {}".format(min(distance_list)))


if __name__ == "__main__":
    main()
