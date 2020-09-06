from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

from .tasks import get_weather_data

class WeatherUpdateView(generic.View):
    def get(self, request, *args, **kwargs):
        cities = City.objects.all()
        for city in cities:
            get_weather_data.delay(city.name)

        messages.add_message(request, messages.INFO,
                            'Weather update task started.')
        return HttpResponseRedirect(reverse('home'))