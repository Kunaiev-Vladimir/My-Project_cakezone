from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacts

# Create your views here.

def index(request):
    #1return HttpResponse("Contacts Index Page")
    #2return render(request, 'contacts.html')
    context = {
        'contacts': Contacts.objects.first()
    }
    return render(request, 'contacts.html', context = context)