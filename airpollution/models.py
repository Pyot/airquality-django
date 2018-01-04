from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField (User, related_name='profile', on_delete=models.CASCADE)
    city = models.CharField( max_length=100, blank=True)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



# class CtrackUser(AbstractUser):
#     date_of_birth = models.DateField(help_text='YYYY-MM-DD format')
#     location = models.CharField(max_length=255, null=True, blank=True)


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length = 256, unique = True)

    def __str__(self):
        return self.city

class Station(models.Model):
    aqi = models.IntegerField()
    google_country = models.CharField(max_length = 256)
    google_info = models.CharField(max_length = 512)
    google_town = models.ForeignKey(City, on_delete = models.CASCADE)
    lat = models.DecimalField(max_digits= 15, decimal_places=12)
    lon = models.DecimalField(max_digits= 15, decimal_places=12)
    station_name = models.CharField(max_length= 512)
    uid = models.IntegerField(unique = True)
    url = models.URLField()

    def __str__(self):
        return str(str(self.uid) + " " + str(self.google_town))

class Pollution(models.Model):
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    station_name = models.ForeignKey(Station, on_delete = models.CASCADE, related_name = 'pollution')
    pm25 = models.FloatField(null = True, blank = True)
    pm10 = models.FloatField(null = True, blank = True)
    o3 = models.FloatField(null = True, blank = True)
    no2 = models.FloatField(null = True, blank = True)
    so2 = models.FloatField(null = True, blank = True)
    nh3 = models.FloatField(null = True, blank = True)
    pb = models.FloatField(null = True, blank = True)
    aqi = models.FloatField(null = True, blank = True)
    p = models.FloatField(null = True, blank = True)
    h =  models.FloatField(null = True, blank = True)
    t = models.FloatField(null = True, blank = True)
    status = models.CharField(null = True, blank = True, max_length = 128)
    time = models.CharField(null = True, blank = True, max_length = 256)

    def __str__(self):
        return str(self.station_name)
