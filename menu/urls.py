from django.urls import path
from .views import index

name = 'menu'

urlpatterns = [
    path('', index, name = 'index'),
   
]