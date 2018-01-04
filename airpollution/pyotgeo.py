from math import sin, cos, sqrt, atan2, radians

#distance between two point on map.
#It will compare two point from google api request and list of station
def distance(lat1a, lon1a, station_list):
    R = 6373.0
    distance_list = []
    for station in station_list:

        lat1 = radians(lat1a)
        lon1 = radians(lon1a)
        lat2 = radians(station[1])
        lon2 = radians(station[2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        # disctance in km
        distance = R * c
        station_details = [station[0], distance]
        distance_list.append(station_details)

    #gen = (x for x in distance_list)
    #lowest_distance = min(gen,key=itemgetter(1))
    distance_list.sort(key=lambda x: x[1])
    return distance_list
