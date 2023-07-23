from django.shortcuts import render
from country.models import Country
from food.models import FoodRecipe, FoodCategory
import requests


# Create your views here.

def index(request):
    q = FoodCategory.objects.all()
    print(q)
    q = q.order_by('name')

    return render(request, 'food/index.html', {'data': q})


def search_result(request):
    return render(request, 'country/search_result.html', )


def category(request, cat_name):
    q = FoodCategory.objects.get(name=cat_name)
    return render(request, 'food/category.html', {'data': q})
