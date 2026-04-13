from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff

# Create your views here.

def index(request):
    #1 return HttpResponse("Masters Index Page")
    #2 return render(request, 'staff.html')
    
    staff = Staff.objects.filter(is_visible=True).order_by('sort')
    context = {
        'staff': staff
    }
    return render(request, 'staff.html', context = context)