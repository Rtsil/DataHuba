from django.shortcuts import render


# Create your views here.

def country(request):
    return render(request, 'country/index.html', {})
