from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #1 return HttpResponse("Masters Index Page")
    return render(request, 'staff.html')