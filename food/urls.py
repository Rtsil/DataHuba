from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='food_home'),
    path('search/', views.search_result, name='food_search'),
    path('<str:cat_name>', views.category, name='category')
    # path('<str:food_name>', views.country, name='food')
]
