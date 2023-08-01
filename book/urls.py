from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='book_home'),
    path('search/', views.search_result, name='search_book'),
    path('<int:book_index>', views.selected_book, name='book')
]
