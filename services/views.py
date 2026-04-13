from django.shortcuts import render
#1from django.http import HttpResponse
#from .models import Service
from menu.models import Category 

# Create your views here.

def index(request):
    #1return HttpResponse("Services Index Page")
    #2return render(request, 'services.html')
    
    categories = Category.objects.filter(is_vsible=True).order_by('sort')
    context = {
        'categories': categories, 
    }
    return render(request, 'services.html', context=context)