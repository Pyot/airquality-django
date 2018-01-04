import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airquality.settings')

import django
django.setup()
import json
import urllib.parse
import requests

from airpollution.models import City, Station, Pollution

#get data form Station DB
data = Station.objects.all()
#print('Data: ', data)

#pollution_add = Pollution.objects.get_or_create(pm25=pm25, pm10=pm10, o3=o3)[0]
#part of API request
url_main = r'https://api.waqi.info/feed/@'
url_token = r'/?token=17e0fbc5712fd203efceed403b9c1102a4648e79'
#Pollution data storage
pollution_data = {}

for row in data:

    print('======================')
    print('Uid: ', row.uid)
    #print('Station_name; ', row.station_name)
    station_n = row.station_name
    uid =  row.uid
    station_name = Station.objects.filter(station_name = station_n)[0]
    print('HALO==========STATION NAME: ',station_name)
    #create API request
    url_city = url_main + str(uid) + url_token
    print(url_city)
    json_data_city = requests.get(url_city).json()
    if json_data_city['status'] == 'ok':
        #create dict_polution with station pollution data
        dict_pollution = {}
        try:
            for k, v in json_data_city['data']['iaqi'].items():
                print(k)
                dict_pollution[k] = v['v']

            dict_pollution['status'] = json_data_city['status']
            dict_pollution['time'] = json_data_city['data']['time']['s']

        except AttributeError:
            print("AttributeError: 'list' object has no attribute 'items'")
            print("Brak danych na poziomie iaqi lub time  w stacji: ", station_n)
            dict_pollution = {
                'status': 'No Data'
            }
        except Exception as e:
            print('Error: ', e)
            dict_pollution = {
                'status': 'No Data'
            }

        print("============= dict_pollution ========")
        print(dict_pollution)
        #create list for bulk_create
        bulk_pollution=[]
        new_pollution = Pollution()
        for k,v in dict_pollution.items():
            new_pollution.station_name = station_name
            print('Key: ', k)
            print('Value: ', v)

            if hasattr(new_pollution, k):
                setattr(new_pollution, k, v)

        bulk_pollution.append(new_pollution)
        print(bulk_pollution)
        Pollution.objects.bulk_create(bulk_pollution)
    else:
        dict_pollution = {
            'status': 'Sation not working'
        }
        bulk_pollution=[]
        new_pollution = Pollution()
        for k,v in dict_pollution.items():
            new_pollution.station_name = station_name
            print('Key: ', k)
            print('Value: ', v)

            if hasattr(new_pollution, k):
                setattr(new_pollution, k, v)

        bulk_pollution.append(new_pollution)
        print(bulk_pollution)
        Pollution.objects.bulk_create(bulk_pollution)
        print("Stacja nie działa")
