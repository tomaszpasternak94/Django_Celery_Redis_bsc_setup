import requests

from django.conf import settings
from celery import task

@task
def get_weather_data(city):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={api_key}"
    data = requests.get(url).json()

    city, created = City.objects.update_or_create(name=city,
                                                  defaults={
                                                            'temperature': data['main']['temp'],
                                                            'description': data['weather'][0]['description'],
                                                            'icon': data['weather'][0]['icon'],
                                                            'country': data['sys']['country'],
                                                          })