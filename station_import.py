import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airquality.settings')

import django
django.setup()
import json

from airpollution.models import City, Station

json_city_station = open('city_base_google.txt').read()
city_station = json.loads(json_city_station)


def addCityAndStation():
    for k,v in city_station.items():
        #dodajemy miasta do modelu City
        city_name = v['google_town']
        print(city_name)
        city_add = City.objects.get_or_create(city=city_name)[0]
        #dodajemy informacje do moedlu Station
        aqi = v['aqi']
        if aqi == '-':
            aqi = 0
        else:
            aqi = v['aqi']
        google_country = v['google_country']
        google_info = v['google_info']
        lat = v['lat']
        lon = v['lon']
        station_name = v['station_name']
        uid = v['uid']
        print(uid)
        url = v['url']
        #print(aqi, google_country, google_info, lat, lon, station_name, uid, url)
        aqi_add = Station.objects.get_or_create(aqi = aqi, google_country = google_country, google_town = city_add, google_info = google_info, lat = lat, lon = lon, station_name = station_name , uid =  uid, url = url)[0]

if __name__ == '__main__':
    print ("Start Adding!")
    addCityAndStation()
    print("Adding completed")
