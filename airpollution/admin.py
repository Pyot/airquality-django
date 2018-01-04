from django.contrib import admin
from airpollution.models import City, Station, Pollution

class StationAdmin(admin.ModelAdmin):
    search_fields =  ['google_town__city', 'station_name', 'uid']
    list_display = ['google_town','station_name', 'uid', 'url']

    class Meta:
        model = Station


class PollutionAdmin(admin.ModelAdmin):
    search_fields = ['station_name__station_name']#ForeignKey Search
    list_display = ['station_name' ,'timestamp', 'pm25', 'pm10', 'o3', 'no2',
                    'so2', 'nh3', 'pb', 'aqi', 'p', 'h', 't']
    class Meta:
        model = Pollution


# admin.site.register(CtrackUser)
admin.site.register(City)
admin.site.register(Station, StationAdmin)
admin.site.register(Pollution, PollutionAdmin)
