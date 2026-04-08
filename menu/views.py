from django.shortcuts import render
from .models import Category

# Create your views here.

def index(request):
    #categories = Category.objects.all()
    #!categories = Category.objects.all().order_by('sort')
    #return None
    #return f'{categories}'
    return render(request, 'menu.html')