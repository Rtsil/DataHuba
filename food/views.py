from django.shortcuts import render
from country.models import Country
from food.models import FoodRecipe, FoodCategory, Meal
import requests


# Create your views here.

def index(request):
    q = FoodCategory.objects.all()
    q = q.order_by('name')

    return render(request, 'food/index.html', {'data': q})


def search_result(request):
    return render(request, 'food/search_result.html', )


def category(request, cat_name):
    q = FoodCategory.objects.get(name=cat_name)
    return render(request, 'food/category.html', {'data': q})


def recipe(request, meal_name):
    return render(request, 'food/recipe.html', {'data': q})


def meals(request):
    q = Meal.objects.all()
    print(q)
    return render(request, 'food/meals.html', {'data': q})


def meal(request, meal_name):
    q = Meal.objects.get(name=meal_name)
    print(q)
    return render(request, 'food/meal.html', {'data': q})
