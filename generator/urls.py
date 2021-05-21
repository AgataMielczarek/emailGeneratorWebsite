from django.urls import path
from . import views
# importowanie z views, kropkę wstawiamy jeżli pobiebramy z tego samego folderu

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name='result'),
    path('about', views.about, name='about')
]
