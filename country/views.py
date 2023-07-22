from django.shortcuts import render
from country.models import Country
import requests

rest_county_url = 'https://restcountries.com/v3.1'


# Create your views here.

def index(request):
    q = Country.objects.all()
    q = q.order_by('name')
    return render(request, 'country/index.html', {'data': q})


def search_result(request):
    search_query = request.GET.get('q', '')
    q = Country.objects.filter(name__icontains=search_query)
    return render(request, 'country/search_result.html', {'data': q})


def country(request, country_name):
    q = Country.objects.get(name__icontains=country_name)
    return render(request, 'country/country.html', {'data': q})

