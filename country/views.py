from django.shortcuts import render
from country.models import Country
import requests

rest_county_url = 'https://restcountries.com/v3.1'


# Create your views here.

def index(request):
    return render(request, 'country/index.html', {})


def search_result(request):
    search_query = request.GET.get('q', '')
    q = Country.objects.get(name__icontains=search_query)
    print(q.flag_emoji)
    if q:
        return render(request, 'country/search_result.html', {'data': q})
    else:
        data = {'status': 'Not Found'}
        return render(request, 'country/search_result.html', data)
