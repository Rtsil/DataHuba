from django.contrib import admin
from .models import FoodRecipe, FoodCategory, Meal


# Register your models here.
admin.site.register(FoodRecipe)
admin.site.register(FoodCategory)
admin.site.register(Meal)