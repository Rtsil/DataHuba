from django.shortcuts import render
import requests
rest_county_url = 'https://restcountries.com/v3.1'

# Create your views here.

def index(request):
    return render(request, 'country/index.html', {})


def search_result(request):
    search_query = request.GET.get('q', '')
    url = f"{rest_county_url}/name/{search_query}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()[0]
        return render(request, 'country/search_result.html', {'data': data})
    else:
        data = {'status': 'Not Found due to an error'}
        return render(request, 'country/search_result.html', data)
