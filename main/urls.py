from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('forecast', views.forecast, name='forecast')
]