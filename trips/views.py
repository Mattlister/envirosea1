from django.shortcuts import render
from .models import Trips

# Create your views here.


def all_trips(request):
    """ View to display trips with search options"""

    trips = Trips.objects.all()

    context = {
        'trips': trips,
    }
    return render(request, 'trips/trips.html', context)
