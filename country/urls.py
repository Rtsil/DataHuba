from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='country_home'),
    path('search/', views.search_result, name='search'),
    path('<str:country_name>', views.country, name='country')
]
