import datetime as dt
import requests
from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry, Point
from .models import WorldBorder


def home(request):
    pnt = Point(28.7041, 77.1025)
    qs = WorldBorder.objects.filter(name='India')
    # ----------------------------------------------------------------------------
    responce = requests.get(
        'https://api.weather.gov/points/38.8894,-77.0352').json()
    # responce = requests.get('https://api.weather.gov/points/{WorldBorder.lon},{WorldBorder.lat}').json()
    data = responce['properties']
    responce1 = requests.get(data['forecast']).json()
    temp = responce1['properties']
    periods1 = temp['periods']
    context = {
        'qs': qs,
        "periods1": periods1
    }
    return render(request, 'home.html', context)
