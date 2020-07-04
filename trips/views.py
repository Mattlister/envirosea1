from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ View to display all products with search options"""

    trips = Product.objects.all()

    context = {
        'trips': trips,
    }
    return render(request, 'trips/trips.html', context)
