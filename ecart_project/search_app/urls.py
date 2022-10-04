from django.urls import path

from search_app import views

app_name = 'search_app'

urlpatterns = [
    path('', views.Search, name='search'),
    ]