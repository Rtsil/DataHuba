#! /home/tsilavo/Documents/country_data/venv/bin/python3
import os
import django
import sys
# sys.path.append('/home/tsilavo/Documents')

import requests

# # Replace 'path/to/your/django_project' with the actual path to your Django project directory
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "country_data.config.settings")
# django.setup()
#
from food.models import FoodRecipe, FoodCategory, Meal
def get_food_cat():
    url_category = 'https://www.themealdb.com/api/json/v1/1/categories.php'
    response = requests.get(url_category).json()['categories']
    # print(response)
    for cat in response:
        new_cat = FoodCategory(name=cat["strCategory"], image=cat["strCategoryThumb"],
                               description=cat['strCategoryDescription'])
        new_cat.save()

import requests
from food.models import FoodRecipe, FoodCategory, Meal
def get_recipes_from_cat():

    url_category = 'https://www.themealdb.com/api/json/v1/1/categories.php'
    response = requests.get(url_category).json()['categories']
    for cat in response:
        url_list_meal = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={cat['strCategory']}"
        response = requests.get(url_list_meal).json()['meals']
        for meal in response:
            new_meal = Meal(name=meal['strMeal'], image=meal['strMealThumb'])
            new_meal.save()

def main():
    get_food_cat()

if __name__=='__main__':
    main()
# new_food = FoodRecipe(meal_name=meal_name, category=category, area=area,
#                           instructions=instructions, meal_image=meal_image,
#                           tags=tags, youtube_link=youtube_link, ingredients_and_measures=ingredients_and_measures)
