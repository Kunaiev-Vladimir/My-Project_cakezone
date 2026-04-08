from django.shortcuts import render
#1from django.http import HttpResponse

# Create your views here.

def index(request):
    #1return HttpResponse("Services Index Page")
    return render(request, 'services.html')