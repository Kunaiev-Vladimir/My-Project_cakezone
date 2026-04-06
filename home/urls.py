from django.urls import path
from .views import index

name = 'home'

urlpatterns = [
    path('', index, name = 'index'),
   
]