from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='food_home'),
    path('search/', views.search_result, name='food_search'),
    path('category/<str:cat_name>', views.category, name='category'),
    path('meals', views.meals, name='meals'),
    path('<str:meal_name>', views.meal, name='meal'),
    path('<str:meal_name>', views.recipe, name='recipe')

]
