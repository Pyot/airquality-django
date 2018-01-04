from django.conf.urls import url
from airpollution import views

app_name = 'airpollution'

urlpatterns = [
    url(r'^stations/$', views.StationView.as_view(), name='station'),
    url(r'^stations/(?P<pk>\d+)/$', views.PollutionDetail.as_view(), name='station_detail'),
    url(r'^choose_stations/$', views.station_list, name='station_list'),
    url(r'^nearest_station/$', views.nearest_station, name='nearest_station'),
]
