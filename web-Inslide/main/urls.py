from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('slide',  views.slide, name='slide'),
    path('get_id',  views.get_id, name='get_id'),
    path('get_url',  views.get_url, name='get_url'),
]