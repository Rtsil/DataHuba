from django.contrib import admin
from .models import FoodRecipe, FoodCategory


# Register your models here.
admin.site.register(FoodRecipe)
admin.site.register(FoodCategory)