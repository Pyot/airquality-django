from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import urllib.parse
import requests
import json
from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
from . import models
from . import pyotgeo
from allauth.account.forms import LoginForm
from airpollution.forms import AirLoginForm
from django.contrib.auth.models import User


class StationView(ListView):
    context_object_name = 'stations'
    model = models.Station
    ordering = ['google_town__city']
    paginate_by = 20

class PollutionDetail(DetailView):
    context_object_name = 'station_pollution'
    model = models.Station
    template_name = 'airpollution/pollution_list.html'

def station_list(request):
    queryset_list= models.Pollution.objects.all().order_by('-timestamp')
    query = request.GET.get('q')
    print(type(queryset_list))
    print(queryset_list)
    if query:
        queryset_list = queryset_list.filter(station_name__station_name__icontains=query).order_by('station_name__uid','-timestamp').distinct('station_name__uid')
        print("SET: ", set(queryset_list))
        print("NO SET: ", queryset_list)
        for station in queryset_list:
            print(station.station_name.uid)
        print(queryset_list)
    context = {
        "station_list_a": queryset_list,
    }

    return render(request, "airpollution/choose_station.html", context)

def nearest_station(request):

    queryset_list= models.Pollution.objects.all().order_by('-timestamp')
    queryset_geo= models.Station.objects.all()
    #google map used to get geolocation after town and town street
    main_api ='http://maps.googleapis.com/maps/api/geocode/json?'

    lat, lon = 00, 00
    queryset_closest_station_data = ''
    closest_station_5 = []
    closest_station_6_data = []
    #guery for latitude and lontitude station. leater is passed to def distance
    station_list= models.Station.objects.values_list('uid','lat','lon')

    username = None

    if request.user.is_authenticated():

        username = request.user.profile.city
        address = username
        if request.GET.get('q'):
            address = request.GET.get('q')
    else:
        address = request.GET.get('q')

    if address:
        print("address po ", address)
        url =  main_api + urllib.parse.urlencode({'address': address})
        json_data = requests.get(url).json()
        json_status =  json_data['status']
        if json_status == 'OK':
             lat = json_data['results'][0]['geometry']['location']['lat']
             lon = json_data['results'][0]['geometry']['location']['lng']
        #closest station from serach box query. sorted from the closest to the furthest
        closest_station = pyotgeo.distance(lat, lon, station_list)
        #list of 5 closest station
        closest_station_6 = closest_station[0:6]

        for i, station in enumerate(closest_station_6):
            queryset_closest_6 = queryset_list.filter(station_name__uid__icontains=closest_station[i][0]).order_by('station_name__uid','-timestamp').distinct('station_name__uid')
            query = queryset_closest_6[0]
            setattr(query,'distance', round(station[1],1))

            closest_station_6_data.append(query)


    paginator = Paginator(closest_station_6_data, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        closest = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        closest = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        closest = paginator.page(paginator.num_pages)

    context= {
        'closest_station_6_data': closest,
        'page_request_var': page_request_var,
        'lat': lat,
        'lon': lon,
        'login_form': AirLoginForm(),
        'address': address,

    }

    return render(request, "airpollution/nearest_station.html", context)
