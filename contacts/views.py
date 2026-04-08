from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #1return HttpResponse("Contacts Index Page")
    return render(request, 'contacts.html')